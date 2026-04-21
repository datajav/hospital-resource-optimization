# 🏥 Hospital Forecasting & Optimization

> Optimizing hospital bed and staff allocation across Jamaica using constrained optimization models — demonstrating how mathematical programming can reduce bottlenecks in critical care units and improve resource utilization.

---

## 📌 Project Overview

This project models hospital bed demand and capacity across Jamaica by combining:

- **Synthetic patient inflow generation** — Poisson arrivals with seasonal adjustments
- **Demand forecasting** — Per-facility models built with [Prophet](https://facebook.github.io/prophet/)
- **Resource optimization** — Bed allocation to minimize overflow using [PuLP](https://coin-or.github.io/PuLP/)

---

## 🎯 Problem Statement

Hospitals regularly face compounding resource challenges:

| Challenge | Description |
|---|---|
| 🛏️ Bed scarcity | Limited ICU and general ward capacity |
| 👩‍⚕️ Staff shortages | Uneven coverage across shifts |
| 📈 Unpredictable demand | Volatile patient arrival patterns |

**Goal:** Allocate resources efficiently to minimize wait times and maximize patient coverage.

---

## 📁 Project Structure

```
hospital-resource-optimization/
├── casestudy/      # summary findings
├── data/           # Raw and processed datasets
├── figures/        # charts and plots
├── notebooks/      # Interactive exploration and modeling
└── src/            # Reusable Python modules
```

---

## 📊 Results

- ✅ Reduced ICU bottlenecks considerably
- ✅ Improved staff utilization across shifts
- ✅ Generated allocation plans that balance patient demand with available resources

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/datajav/hospital-resource-optimization
cd hospital-resource-optimization
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Launch the notebook**
```bash
jupyter notebook HospitalOptimization.ipynb
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-blue?style=flat)
![PuLP](https://img.shields.io/badge/PuLP-Optimization-green?style=flat)



 