# 🛍️ Customer Segmentation Using Machine Learning

This is a personal project where I explored customer behavior using machine learning techniques to identify distinct customer segments and provide data-driven marketing strategies. The goal was to use unsupervised learning to uncover patterns in purchasing behavior.

---

## 📊 Project Overview

Customer segmentation helps businesses personalize marketing and enhance customer engagement. In this project, I applied both **K-Means** and **Hierarchical Clustering** on retail data to analyze customer demographics, behavior, and purchasing trends.

---

## 📁 Data Preprocessing

### ✅ Cleaning & Imputation
- Missing **numerical** values filled with **median**
- Missing **categorical** values filled with **mode**
- Removed duplicate records  
- Outliers identified and removed using the **IQR method**  
- Final cleaned dataset saved as a new CSV for further analysis  
- 📸 _(screenshot)_

### 📐 Feature Standardization
- Used `StandardScaler` to normalize values
- Selected features:
  - `Purchase Amount (USD)`
  - `Age`
  - `Previous Purchases`

---

## 📈 Exploratory Data Analysis (EDA)

### 📊 Visualizations
- **Histograms** with KDE for:
  - Age, Purchase Amount, Review Rating, Previous Purchases  
  - 📸 _(screenshot)_
- **Bar plots** for:
  - Gender, Item Purchased, Location, Color, Season  
  - 📸 _(screenshot)_
- **Correlation heatmap** to identify numeric relationships  
  - 📸 _(screenshot)_
- **Pairplot** to explore patterns by age and purchase frequency  
  - 📸 _(screenshot)_

### 🔍 Key Insights
- Most purchases occurred in **Winter**
- **Maroon** was the most common color purchased
- **Previous Purchases** had a moderate positive correlation with **Purchase Amount**
- Clear behavior differences between **young** and **older** customers

---

## 🤖 Clustering Models

### 📌 K-Means Clustering
- Used **Elbow Method** to determine `k = 5`  
  - 📸 _(screenshot)_
- Applied K-Means to create `Cluster_KMeans` labels
- Visualized clusters using scatter plots of `Purchase Amount vs Age`  
  - 📸 _(screenshot)_

#### Cluster Summaries:
- **Cluster 0**: Older, frequent, high spenders  
- **Cluster 2**: Younger, low spenders  
- **Cluster 4**: Younger, high spenders  

---

### 🌿 Hierarchical Clustering
- Used **Ward’s Method** to generate dendrograms and identify 4 clusters  
  - 📸 _(screenshot)_
- Applied Agglomerative Clustering and labeled results as `Cluster_Hierarchical`
- Visualized results with scatterplots  
  - 📸 _(screenshot)_

---

## 💡 Insights & Business Recommendations

### 🧠 Segment Analysis
- **Cluster 0**: Loyal older customers with high spending
- **Cluster 2**: Budget-conscious younger customers
- **Cluster 4**: Trendy, younger high spenders

### 📢 Strategy Suggestions
- 🎁 **Loyalty Programs** for Cluster 0
- 🛍️ **Seasonal Discounts & Bundles** for Cluster 2
- 📲 **Targeted Trend Ads** for Cluster 4

---

## 🧰 Tools & Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- CoLab

---

## 👨‍💻 Created By

**Tawhid Khan**  

---

