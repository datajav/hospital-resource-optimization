# Hospital Forecasting & Optimization

This project models hospital bed demand and capacity across Jamaica using:
- **Synthetic patient inflow generation** (Poisson arrivals + seasonality)
- **Forecasting with Prophet** (per facility)
- **Optimization with PuLP** (bed allocation to minimize overflow)

## Project Structure
- `data/` → raw and processed datasets
- `notebooks/` → interactive exploration and modeling
- `src/` → reusable Python scripts
- `reports/` → figures and summary findings

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. 	Run notebooks in order:
• 	01_EDA.ipynb
• 	02_SyntheticData/ipynb


Dependencies
• 	pandas
• 	numpy
• 	matplotlib
• 	seaborn
• 	prophet
• 	pulp
