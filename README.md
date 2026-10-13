## 🔥 Interactive Crime Hotspot Map

👉 **Live map:**  
https://sochiencode.github.io/crime-trend-analysis-cleveland/

The map visualises spatial concentrations of recorded crime in Cleveland (UK)
using the existing Folium HeatMap method and open street-crime data.
The map covers January 2023–November 2025; it excludes outcome and stop-and-search records.


---

## Run the analysis

Use Python 3.12 (tested with 3.12.14). Run these commands from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab crime_trends_analysis.ipynb
```

In Jupyter, restart the kernel and run all cells. For a fresh-kernel, noninteractive run that stops at the first error:

```bash
jupyter nbconvert --to notebook --execute --inplace crime_trends_analysis.ipynb --ExecutePreprocessor.timeout=180
```

The notebook regenerates `assets/monthly_trends.png`, `data/monthly_crime_trends_uk.csv`, `cleveland_crime_hotspots.html`, and `docs/index.html`.
The CSV retains its original filename for compatibility; its counts describe Cleveland, not the whole UK.
The bundled data contains 35 consecutive months, January 2023–November 2025. Street crime, outcomes, and stop-and-search remain separate files; only `*-street.csv` is loaded here. No Google Colab or external data download is required. Map tiles and JavaScript assets need internet access when viewing the HTML.

The missing-file experiments were removed because they referenced CSVs absent from this repository. The local-area analysis now defines its Cleveland street-crime table before use. Package installation is handled by `requirements.txt` rather than notebook cells. Monthly aggregation, seasonal averages, and heatmap settings are retained; this repair introduces no new crime findings. Power BI is optional and its dashboard file is not included.

## Key Analyses

### 1. Temporal Crime Trends
- Monthly aggregation of reported crimes
- Identification of seasonal and long-term trends
- Comparison across crime categories

📈 *Example output:*  
![Monthly Crime Trends](assets/monthly_trends.png)

---

### 2. Crime Type Distribution
- Frequency analysis of reported crime types
- Identification of dominant offences across the period
- Comparison of variability between crime categories

---

### 3. Spatial Analysis
- Geographic plotting using latitude and longitude
- Folium heatmap to visualise concentrations of recorded street crime
- Visual separation of dense vs low-frequency areas


---

### 4. Power BI Dashboard
An interactive dashboard was created to allow:
- Time-based filtering using a date slicer
- Crime type filtering
- Dynamic map and trend updates

The dashboard enables **non-technical users** to explore crime patterns without interacting with code.

---

## Key Insights (Summary)
- Certain crime categories consistently dominate monthly totals
- Clear temporal patterns are observable across the period
- Crime incidents show strong spatial clustering in specific urban areas
- Interactive visualisation significantly improves insight accessibility

*(Detailed insights are documented within the notebook and dashboard.)*

---

## Limitations
- Analysis is limited to reported crimes only
- No demographic or socioeconomic variables included
- Spatial accuracy depends on available coordinate precision
- Forecasting beyond short-term horizons was not included

---

## Future Improvements
- Add short-term crime forecasting models
- Introduce intervention scenario modelling (e.g. patrol increases)
- Enrich data with population or deprivation indices
- Publish dashboard to Power BI Service for public access

---

## Author
**Anamum Ifesochi**  
Data Analyst | Crime & Intelligence Analysis  
📍 UK

---

## License
This project is for **educational and portfolio purposes only**.  
Data remains the property of its original source.

