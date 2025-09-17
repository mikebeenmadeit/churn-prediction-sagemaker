
## 📅 Week 2 Progress

### Day 1 — Setup & Data Prep ✅
- Created a new SageMaker Notebook instance  
- Connected to my churn dataset stored in S3 (`customer-churn-data-michael`)  
- Loaded the dataset into a Pandas DataFrame  
- Performed exploratory data analysis (EDA):  
  - Checked schema (21 columns, 7043 rows)  
  - Looked at churn distribution (imbalanced classes)  
  - Verified missing values  

**Deliverable:**  
`01-data-prep.ipynb` — saved in repo & pushed to GitHub.  

---

## 📂 Repo Contents
- `01-data-prep.ipynb` — Data load & EDA notebook  

---

### Day 2 — Train XGBoost Churn Model ✅
- Trained cost-efficient **local XGBoost** classifier (no SageMaker training quotas required)
- Features: one-hot encoded categoricals, numeric coercion, NA fill; stratified 80/20 split
- Saved model locally and uploaded artifact to S3



**Notebook:** `02-train-model.ipynb`

**Artifacts**
-Metrics: `metrics.txt`

### Next Steps (Day 3+)
- Optional: **Hyperparameter tuning** (XGBoost grid with AUC)
- Package inference code and **deploy endpoint (real-time or serverless)**  
- Add an **API Gateway + Lambda** wrapper and a tiny CLI / Postman demo
- Write a short **“Business Value of Churn Prediction”** note (cost savings, retention lift)



