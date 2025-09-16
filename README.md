
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

## Next Steps (Day 2+)
- Train churn prediction model (XGBoost in SageMaker)  
- Deploy endpoint + wrap with API Gateway + Lambda  
- Test predictions with Postman/cURL  
- Add API demo + business value report  
EOF

