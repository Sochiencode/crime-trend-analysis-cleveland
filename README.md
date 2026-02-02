# crime-trend-analysis-cleveland
Time-series and seasonal analysis of recorded crime trends in Cleveland (UK) using Python and Power BI.
# Crime Trend and Spatial Analysis: Cleveland (UK)

## Overview
This project presents a time-series and spatial analysis of recorded crime in the **Cleveland Police Force Area (UK)**. Using Python-based analytical workflows, the study explores temporal trends, seasonal variation, and spatial concentration of crime at both incident and neighbourhood (LSOA) level.

The project is designed to demonstrate **policy-relevant crime analysis**, combining exploratory hotspot mapping with administrative boundary-based choropleth visualisation.

---

## Research Objectives
- Identify long-term and seasonal crime trends in Cleveland
- Explore spatial clustering of crime incidents using hotspot analysis
- Aggregate crime data at **Lower Layer Super Output Area (LSOA)** level
- Produce policy-grade spatial visualisations suitable for public-sector decision-making

---

## Data Sources
- UK Police Open Data (Recorded Crime)
- Office for National Statistics (ONS) – LSOA Boundary Shapefiles (2021)

---

## Methodology
### Temporal Analysis
- Monthly aggregation of recorded crime
- Identification of seasonal patterns and trend shifts
- Crime type comparison by volume

### Spatial Analysis
Two complementary spatial approaches were used:

**1. Hotspot Analysis (Point-Based)**  
Incident-level latitude and longitude coordinates were visualised using a kernel-density-inspired heatmap to identify high-concentration areas of crime activity.

**2. LSOA Choropleth Mapping (Area-Based)**  
Crimes were aggregated by LSOA and merged with official ONS boundary geometries. Choropleth maps were produced to highlight spatial variation across neighbourhoods, enabling comparison within a policy-relevant administrative framework.

---

## Key Outputs
- Interactive crime hotspot heatmap
- LSOA-level choropleth map of total recorded crime
- Ranked LSOAs by crime volume
- Seasonal crime trend analysis

---

## Tools & Technologies
- Python (pandas, geopandas, folium, matplotlib)
- Jupyter Notebook (VS Code)
- Open Government Data
- GIS-based spatial analysis techniques

---

## How to Run the Project
```bash
pip install -r requirements.txt


