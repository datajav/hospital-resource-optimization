import pandas as pd 
import numpy as np

n_days=120
facility_ids = ["01-24", "01-23", "01-20", "01-02", "01-03", "01-21", "01-19", "PRIV01", "PRIV02", "PRIV03", "PRIV04", "PRIV05", "03-18", "04-16", "05-08", "05-17", "06-05", "07-10", "08-01", "PRIV06", "PRIV07", "PRIV08", "13-12", "14-07", "14-11", "01-22"]
departments = ["ER", "ICU", "Maternity"]

seasonal_factors = {
    "Jan": 1.0, 
    "Feb": 1.3, #30% increase in February due to the flu
    "Mar": 1.2, #20% increase in March due to the tail end of flu season
    "Apr": 0.9, #10% decrease in April as flu season ends
}

records = []

date_range = pd.date_range(start="2026-01-01", periods=n_days)

for date in date_range:
    month = date.strftime("%b")
    season_factor = seasonal_factors.get(month,1.0)
     
    for facility in facility_ids:
       for dept in departments:
         
        if dept == "ER":
           lam = 20 
        elif dept == "ICU":
           lam = 10
        else: # Maternity
           lam = 5 

        arrivals = np.random.poisson(lam * season_factor)

        records.append({
           "Date": date, 
           "Facility_ID": facility,
           "Departments": dept,
           "Predicted_Arrivals": arrivals,
           })


synthetic_df = pd.DataFrame(records)
print(synthetic_df)

synthetic_df.to_csv("synthetic_hospital_arrivals.csv", index=False)