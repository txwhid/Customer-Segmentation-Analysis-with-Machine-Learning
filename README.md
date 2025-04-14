# 🛍️ Customer Segmentation Using Machine Learning

This is a personal project where I explored customer behavior using machine learning techniques to identify distinct customer segments and provide data-driven marketing strategies.

---

## 📊 Project Overview

Customer segmentation helps businesses personalize marketing and enhance customer engagement. In this project, I applied both **K-Means** and **Hierarchical Clustering** on retail data to analyze customer demographics, behavior, and purchasing trends.

---

## 📁 Data Preprocessing

### ✅ Cleaning & Imputation

- Missing **numerical** values filled with **median**
- Missing **categorical** values filled with **mode**

![Screenshot](Screenshot 2025-04-14 at 6.36.07 PM.png)

- Removed duplicate records

![Screenshot](Screenshot 2025-04-14 at 6.36.22 PM.png)

- Outliers removed using IQR method

![Screenshot](Screenshot 2025-04-14 at 6.36.33 PM.png)

- Outlier function applied iteratively across columns

![Screenshot](Screenshot 2025-04-14 at 6.36.45 PM.png)

- Final cleaned data saved to a CSV

![Screenshot](Screenshot 2025-04-14 at 6.36.55 PM.png)

---

## 📈 Exploratory Data Analysis (EDA)

- **Histograms** with KDE for Age & Purchase Amount:

![Screenshot](Screenshot 2025-04-14 at 6.37.15 PM.png)

---

## 🤖 Clustering Models

### 📌 K-Means Clustering

- Used Elbow Method to determine optimal k
- Applied clustering and visualized with scatter plot:

![Screenshot](Screenshot 2025-04-14 at 6.37.27 PM.png)

### 🌿 Hierarchical Clustering

- Generated dendrogram to determine cluster groups:

![Screenshot](Screenshot 2025-04-14 at 6.37.36 PM.png)

---

## 💡 Insights & Business Recommendations

### 🧠 Segment Analysis

- **Cluster 0**: Older customers, high-value, loyal
- **Cluster 2**: Younger, low spenders
- **Cluster 4**: Younger, high spenders

### 📢 Strategy Suggestions

- 🎁 **Loyalty Programs** for Cluster 0
- 🛍️ **Seasonal Discounts** for Cluster 2
- 📲 **Targeted Trend Ads** for Cluster 4

---

## 🧰 Tools & Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 👨‍💻 Created By

**Sabeel Khan**  
*Big Data & Machine Learning Enthusiast*  
Lakehead University – COMP 4311

---
