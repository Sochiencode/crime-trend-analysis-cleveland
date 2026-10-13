"""Interactive Cleveland Police recorded crime and ASB portfolio dashboard."""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parent
ASB = 'Anti-social behaviour'
st.set_page_config(page_title='Cleveland | Recorded Events', page_icon='📊', layout='wide')

@st.cache_data
def load_data():
    data = pd.read_csv(ROOT / 'data/monthly_crime_trends_uk.csv', parse_dates=['Month'])
    geo = pd.read_csv(ROOT / 'data/dashboard_geography.csv', parse_dates=['Month'])
    return data, geo

data, geo = load_data()
st.title('Cleveland: recorded crime & anti-social behaviour')
st.caption('January 2023–November 2025 · Cleveland Police open street data · Ifesochi Abanum')
st.sidebar.header('Explore the records')
months = sorted(data.Month.unique())
period = st.sidebar.select_slider('Month range', options=months, value=(months[0],months[-1]), format_func=lambda x: pd.Timestamp(x).strftime('%b %Y'))
include_asb = st.sidebar.checkbox('Include anti-social behaviour', value=True)
available = sorted(data['Crime type'].unique())
if not include_asb:
    available.remove(ASB)
categories = st.sidebar.multiselect('Categories', available, default=available)
selected = data[data.Month.between(*period) & data['Crime type'].isin(categories)]
if selected.empty:
    st.info('Select at least one category with records in this date range.')
    st.stop()

st.sidebar.caption('Filters affect the overview and map. Year comparisons use a separate matching-month window.')
overview, comparison, geography, methods = st.tabs(['Overview','Year comparisons','Geographic patterns','Methods & limitations'])
with overview:
    total = int(selected.crime_count.sum())
    asb = int(selected.loc[selected['Crime type'].eq(ASB),'crime_count'].sum())
    cols = st.columns(4)
    cols[0].metric('Street-data records', f'{total:,}')
    cols[1].metric('Anti-social behaviour', f'{asb:,}')
    cols[2].metric('Other crime-category records', f'{total-asb:,}')
    cols[3].metric('Months selected', selected.Month.nunique())
    monthly = selected.groupby('Month',as_index=False).crime_count.sum()
    st.plotly_chart(px.line(monthly,x='Month',y='crime_count',markers=True,labels={'crime_count':'Recorded events'},title='Monthly recorded-event volume'),width='stretch')
    shares = selected.groupby('Crime type',as_index=False).crime_count.sum().sort_values('crime_count')
    st.plotly_chart(px.bar(shares,x='crime_count',y='Crime type',orientation='h',labels={'crime_count':'Recorded events'},title='Category composition'),width='stretch')
    st.download_button('Download filtered monthly counts',selected.to_csv(index=False),'cleveland_filtered_counts.csv','text/csv')
with comparison:
    st.subheader('Compare the same months across years')
    end_month = st.slider('January through',1,11,11,format='%d')
    st.caption('Uses the selected categories and all three years, independently of the overview date range. December is excluded because 2025 December is unavailable.')
    comp = data[data['Crime type'].isin(categories) & (data.Month.dt.month <= end_month)].copy()
    comp['Year'] = comp.Month.dt.year
    yearly = comp.groupby('Year',as_index=False).crime_count.sum()
    yearly['Change (%)'] = yearly.crime_count.pct_change()*100
    st.plotly_chart(px.bar(yearly,x='Year',y='crime_count',text_auto=',',labels={'crime_count':'Recorded events'},title='Matching-month recorded counts'),width='stretch')
    st.dataframe(yearly.rename(columns={'crime_count':'Records'}),hide_index=True,width='stretch')
    st.caption('Changes in recorded counts do not prove equivalent changes in underlying crime.')
    st.subheader('Descriptive calendar-month averages')
    totals = data[data['Crime type'].isin(categories)].groupby('Month',as_index=False).crime_count.sum()
    totals['Calendar month'] = totals.Month.dt.month
    seasonal = totals.groupby('Calendar month').agg(Average=('crime_count','mean'),Observations=('crime_count','size')).reset_index()
    st.plotly_chart(px.bar(seasonal,x='Calendar month',y='Average',hover_data=['Observations'],title='Average monthly total for selected categories'),width='stretch')
    st.caption('This dashboard averages monthly totals; the notebook’s per-category seasonal chart uses a different measure. December has two years of observations; other months have three. These averages do not establish recurring seasonal effects.')
with geography:
    st.subheader('Recorded-event concentrations')
    filtered_geo = geo[geo.Month.between(*period) & geo['Crime type'].isin(categories)]
    points = filtered_geo.groupby(['lat','lon'],as_index=False).records.sum()
    st.caption(f'{int(points.records.sum()):,} records represented in coordinate bins rounded to two decimal places. Bin centres are approximate, not incident addresses.')
    st.plotly_chart(px.scatter_map(points,lat='lat',lon='lon',size='records',color='records',size_max=35,zoom=8,center={'lat':54.57,'lon':-1.24},map_style='carto-positron',hover_data={'records':True,'lat':False,'lon':False},height=560,color_continuous_scale='Teal'),width='stretch')
    st.caption('Circle size and colour indicate counts, not population-adjusted risk. This binned map differs from the notebook’s smoothed heatmap. No statistical clustering test was performed. The background map requires internet access.')
with methods:
    st.markdown('''### Source and preparation
Only `*-street.csv` files enter this analysis. Outcome and stop-and-search records remain separate. The full dataset has **269,438 records**, including **50,402 anti-social-behaviour records**, across **35 months and 14 categories**. All **490 monthly/category counts** were reconciled to the committed export.

### Interpretation
- Reporting and recording practices affect these counts; they do not capture every event.
- Anti-social behaviour must not be described as entirely criminal offences.
- Published coordinates are not exact incident locations. Geographic bins are for exploration.
- No population denominators, causal modelling, forecasting or statistical cluster tests are included.
- Power BI dashboard functionality is not verified because its project file is absent.

### Project provenance
Original analysis by Ifesochi Abanum. Codex assisted with reproducibility repairs and development of this dashboard. Dashboard calculations and map summaries are checked against the project data.
''')
    st.link_button('View source and analysis on GitHub','https://github.com/Sochiencode/crime-trend-analysis-cleveland')
