# Inventory Forecasting Optimization

Forecasting-driven inventory optimization using time series modeling and machine learning for retail sales.

---

## 📘 Project Overview

Retail businesses face a constant challenge in balancing stock levels — overstock increases holding costs, while stockouts harm sales and customer trust. This project addresses this challenge through a data-driven approach, combining:

- Time Series Forecasting (`Prophet`)
- Machine Learning Models (`Random Forest`, `XGBoost`)
- Inventory Control Logic (Safety Stock & Reorder Points)

---

## 🔧 Features

- Cleaned and preprocessed sales data
- Weekly sales trend analysis and seasonality detection
- Predictive modeling with Prophet, Random Forest, and XGBoost
- Forecast accuracy evaluation using MAE and RMSE
- Safety stock and reorder point calculation for optimized inventory planning
- Visual comparisons of predicted vs. actual sales

---

## 📊 Model Performance

| Metric       | Random Forest | XGBoost |
|--------------|---------------|---------|
| MAE          | 1707.25       | 2785.66 |
| RMSE         | 2412.41       | 3105.48 |
| **Best Fit** | ✅ Random Forest | ❌       |

---

## 🚚 Inventory Impact Summary

| Metric              | Before | After | Improvement |
|---------------------|--------|-------|-------------|
| Overstock Rate      | 20%    | 15%   | 25% ↓       |
| Stockout Rate       | 10%    | 7%    | 30% ↓       |
| Service Level       | 90%    | 95%   | 5.5% ↑      |

---

## 📂 Project Structure

```bash
inventory-forecasting-optimization/
├── README.md                     # Project overview and usage instructions
├── requirements.txt              # Python dependencies
│
├── data/                         # Data files
│   ├── raw/                      # Original input dataset (excluded from Git)
│   └── processed/                # Cleaned and transformed data
│
├── notebooks/                    # Jupyter notebooks for each project phase
│   ├── 01_EDA_and_Preprocessing.ipynb
│   ├── 02_TimeSeries_Prophet.ipynb
│   ├── 03_ML_Models_RF_XGB.ipynb
│   └── 04_Inventory_Optimization.ipynb
│
├── src/                          # Source code for modeling and utilities
│   ├── __init__.py
│   ├── utils.py
│   ├── forecasting.py
│   └── inventory.py
│
├── models/                       # Trained model artifacts
│   ├── xgb_preds.pkl
│   ├── rf_preds.pkl
│   └── y_test.pkl
│
├── visuals/                      # Generated visualizations and plots
│   ├── sales_trends.png
│   └── model_comparisons.png



