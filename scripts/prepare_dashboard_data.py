"""Reconcile street records and prepare compact map data for the dashboard."""
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
frames = [pd.read_csv(p, usecols=['Month', 'Crime type', 'Latitude', 'Longitude']) for p in sorted((ROOT / 'data/raw').rglob('*-street.csv'))]
df = pd.concat(frames, ignore_index=True)
counts = df.groupby(['Month', 'Crime type']).size().rename('crime_count').reset_index()
original = pd.read_csv(ROOT / 'data/monthly_crime_trends_uk.csv')
original['Month'] = pd.to_datetime(original['Month']).dt.strftime('%Y-%m')
pd.testing.assert_frame_equal(counts, original[['Month','Crime type','crime_count']].sort_values(['Month','Crime type']).reset_index(drop=True), check_dtype=False)
valid = df.dropna(subset=['Latitude','Longitude']).copy()
valid = valid[valid.Latitude.between(-90,90) & valid.Longitude.between(-180,180)]
# Round into approximately 1 km latitude cells; these are visual bins, not risk estimates.
valid['lat'] = valid.Latitude.round(2)
valid['lon'] = valid.Longitude.round(2)
geo = valid.groupby(['Month','Crime type','lat','lon']).size().rename('records').reset_index()
geo.to_csv(ROOT / 'data/dashboard_geography.csv', index=False)
assert geo.records.sum() == len(valid)
print(f'Verified {len(counts)} counts; {len(df):,} records; {len(valid):,} mapped; {len(df)-len(valid):,} excluded; {len(geo):,} geographic rows')
