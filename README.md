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
- 	01_EDA.ipynb
-	02_SyntheticData.ipynb
-	03_Prophet_Forecasting.ipynb
-	04_Optimization.ipynb

Dependencies
-	pandas
-	numpy
-	matplotlib
-	seaborn
-	prophet
-	pulp

## Summary of Findings
This report evaluates Jamaica’s hospital system resilience under varying demand scenarios (Normal, Outbreak, Disaster, and Stress Tests) using facility, parish, and system-level optimization models. The analysis highlights capacity bottlenecks, redistribution effects, and national resilience limits.

1. Facility-Level Insights
-	Normal Demand: Most facilities operate within capacity, with negligible overflow.
- 	Outbreak/Disaster: Smaller hospitals consistently overflow first, creating local bottlenecks.
- 	Implication: These facilities require surge capacity planning (beds, staff, or mobile units).

![Alt Text](https://github.com/datajav/hospital-resource-optimization/blob/684680307d4955317bc1b8197828b9b538d78f00/reports/image.png)

2. Parish-Level Insights
- 	Redistribution within parishes reduces overflow compared to facility-only optimization.
- 	Larger parishes (e.g., Kingston) absorb shocks better due to multiple facilities.
- 	Smaller parishes remain vulnerable, even with redistribution.

![Alth Text](https://github.com/datajav/hospital-resource-optimization/blob/1aeca9cba43fcefbd164cfd0552f54d6247c78c8/reports/image-1.png)

3. System-Level Insights
-	Nationally, the system absorbs normal demand comfortably.
- 	With a 10–20% reserve policy, overflow appears even in moderate scenarios, but resilience improves.
- 	In disaster scenarios, total overflow rises significantly, showing system limits.

![Alth Text](https://github.com/datajav/hospital-resource-optimization/blob/3ad1957c5a80b52a786a1206d25b17db5157164e/reports/image-2.png)

4. Stress Test Findings
- 	Seasonal Spikes (Flu Season): Moderate overflow, manageable with parish redistribution.
- 	Policy Constraints (20% Reserve): Overflow increases but strengthens resilience planning.
- 	Regional Shocks (e.g., Kingston surge): Localized crises highlight the need for inter-parish transfers and mobile capacity.

![Alth Text](https://github.com/datajav/hospital-resource-optimization/blob/3ad1957c5a80b52a786a1206d25b17db5157164e/reports/image-3.png)

5. Key Takeaways
• 	Normal demand is manageable at all levels.
• 	Outbreak/disaster scenarios expose vulnerabilities in smaller facilities and parishes.
• 	System-level reserves are essential but create trade-offs (overflow vs. resilience).
• 	Targeted interventions should focus on high-risk facilities and parishes.

6. Recommendations

1. 	Targeted Interventions: Expand capacity at facilities that consistently overflow.
2. 	Policy Planning: Maintain national reserves and develop transfer protocols.
3. 	Scenario Monitoring: Regularly rerun forecasts with updated demand data.
4. 	Stress Preparedness: Include seasonal and regional shocks in planning cycles.
