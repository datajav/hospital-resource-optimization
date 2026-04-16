# Hospital Forecasting & Optimization

## 📌 Project Overview
Optimizing hospital bed and staff allocation using constrained optimization models.
This project demonstrates how mathematical optimization can reduce bottlenecks in critical care units and improve resource utilization.

This project models hospital bed demand and capacity across Jamaica using:
- **Synthetic patient inflow generation** (Poisson arrivals + seasonality)
- **Forecasting with Prophet** (per facility)
- **Optimization with PuLP** (bed allocation to minimize overflow)

## 🎯 Problem Statement
Hospitals often face:

Limited ICU and general ward beds

Staff shortages across shifts

Unpredictable patient arrivals

The goal: allocate resources efficiently to minimize wait times and maximize patient coverage.


## 📋Project Structure
- `data/` → raw and processed datasets
- `notebooks/` → interactive exploration and modeling
- `src/` → reusable Python scripts
- `casestudy/` → figures and summary findings

## 📊 Results
Reduced ICU bottlenecks considerably.

Improved staff utilization across shifts.

Generated allocation plans that balance patient demand with available resources.


## 🚀 How to Run

```bash git clone https://github.com/datajav/hospital-resource-optimization
cd hospital-resource-optimization
pip install -r requirements.txt
jupyter notebook HospitalOptimization.ipynb

Install dependencies:
   pip install -r requirements.txt

 