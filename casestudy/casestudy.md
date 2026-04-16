# 🏥 Hospital Resource Optimization — Case Study

## 1. Problem
Hospitals face recurring challenges in resource allocation:
- Limited ICU and general ward beds
- Staff shortages across shifts
- Unpredictable patient arrivals and demand spikes

These constraints often lead to **bottlenecks in critical care units** and longer patient wait times.  
The objective was to design an optimization model that balances patient demand with available resources.

---

## 2. Data
- **Inputs**: Bed counts, staff availability, patient demand estimates
- **Format**: CSV sample datasets (synthetic but realistic)
- **Scope**: ICU and general wards, multiple shifts

![Distribution of Beds](https://github.com/datajav/hospital-resource-optimization/blob/0dc7e2422b78d15d228d387546a1342c4bdd9041/figures/Distribution%20of%20Beds.png)

---

## 3. Approach
- **Methodology**: Linear programming optimization
- **Tools**: Python, Jupyter Notebook, pandas, PuLP/OR‑Tools
- **Constraints modeled**:
  - Bed capacity per ward
  - Staff availability per shift
  - Patient demand distribution
- **Decision variables**: Allocation of beds and staff across wards and shifts

---

## 4. Results
- Reduced ICU bottlenecks by **X%** (replace with your metric)
- Improved staff utilization across shifts
- Generated allocation plans that balance patient demand with available resources




---

## 5. Deployment
- **Notebook repo**: [Hospital Resource Optimization](https://github.com/datajav/hospital-resource-optimization)
- **Live demo repo**: [Hospital Resource HTML Service](<link to your HTML repo>)
- **Hosting**: GitHub Pages / Vercel for demo

---

## 6. Limitations & Next Steps
- Current model uses synthetic data; real hospital datasets would improve accuracy
- Assumes static demand; future work could incorporate stochastic modeling
- Potential extension: integrate with hospital scheduling systems for real‑time updates

---

## 7. Impact
This project demonstrates how **optimization techniques can directly improve healthcare delivery** by:
- Reducing patient wait times
- Improving staff workload balance
- Enhancing hospital efficiency under resource constraints
