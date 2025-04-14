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
  
![Screenshot 2025-04-14 at 6 41 33 PM](https://github.com/user-attachments/assets/aa33e2b6-3b1a-4a97-9e55-82b68ae67e00)

- Removed duplicate records
  
![Screenshot 2025-04-14 at 6 42 02 PM](https://github.com/user-attachments/assets/e945747e-03b8-4f56-bf54-7e24abe720a6)

- Outliers removed using IQR method
  
![Screenshot 2025-04-14 at 6 42 26 PM](https://github.com/user-attachments/assets/ec32bb21-1ecb-475f-8135-0f111a1e3829)

- Outlier function applied iteratively across columns
  
![Screenshot 2025-04-14 at 6 42 46 PM](https://github.com/user-attachments/assets/527b23c5-b650-4280-be37-e69dd36b697d)

- Final cleaned data saved to a CSV
  
![Screenshot 2025-04-14 at 6 43 02 PM](https://github.com/user-attachments/assets/7f15a564-d1be-4372-8fb7-4b03f34b2c97)

---

## 📈 Exploratory Data Analysis (EDA)

- **Histograms** with KDE for Age & Purchase Amount:
  
![Screenshot 2025-04-14 at 6 43 29 PM](https://github.com/user-attachments/assets/fca768a6-bde3-4b20-8276-adcc4ea2afc2)

---

## 🤖 Clustering Models

### 📌 K-Means Clustering

- Used Elbow Method to determine optimal k
- Applied clustering and visualized with scatter plot:
  
![Screenshot 2025-04-14 at 6 44 13 PM](https://github.com/user-attachments/assets/2fd786d8-ca45-48c5-8504-238441c5520e)

### 🌿 Hierarchical Clustering

- Generated dendrogram to determine cluster groups:
  
![Screenshot 2025-04-14 at 6 44 36 PM](https://github.com/user-attachments/assets/30273a8a-76b1-4938-ae3b-fd04658382e5)

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

## 🧾 Final Conclusion

In this project, I set out to answer the central question:

> **“Can we segment customers based on their purchasing behavior to support more effective marketing strategies?”**

Using unsupervised machine learning techniques — **K-Means** and **Hierarchical Clustering** — I was able to group customers into meaningful clusters based on factors like **age**, **purchase amount**, and **previous purchase frequency**.

### 📌 Key Insights

- 📊 **Spending behavior varies significantly by age**  
  - Some younger customers formed both the lowest and highest spending clusters.
  
- 🔁 **Repeat purchases correlate with higher spending**  
  - Customers with prior purchase history tend to spend more overall.

- 🛍️ **Seasonality and preferences matter**  
  - Purchases peak in winter, and product features like color (e.g., maroon) can influence buying trends.

### 🎯 Outcome

This analysis enabled the creation of **targeted marketing strategies** for different customer types, helping businesses better allocate promotional resources and improve customer engagement. The segmentation approach supports more personalized, data-driven decisions to enhance both **sales performance** and **customer loyalty**.

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
