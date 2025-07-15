# 🚀 SpaceX Falcon 9 Launch Analysis Project

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](#)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat\&label=Contributions\&colorA=red\&colorB=black)](#)

---

## 📖 Project Overview

This project analyzes **SpaceX Falcon 9** rocket launches to predict first-stage landing success. Since SpaceX reuses first stages to reduce cost (e.g., \$62M vs. \$165M by others), predicting successful landings helps estimate launch costs and improve operational efficiency.

---

## 📁 Repository Contents

### 📡 Data Collection

* `jupyter-labs-webscraping.ipynb`: Scrapes Wikipedia using `BeautifulSoup`.
* `jupyter-labs-spacex-data-collection-api-v2.ipynb`: Uses SpaceX REST API to collect launch data.

### 🧹 Data Processing

* `labs-jupyter-spacex-Data wrangling-v2.ipynb`: Cleans and merges datasets.

### 📊 Exploratory Data Analysis

* `jupyter-labs-eda-sql-coursera_sqllite.ipynb`: SQL-based queries and insights.
* `jupyter-labs-eda-dataviz-v2.ipynb`: Visualizations using Seaborn and Matplotlib.

### 🗺️ Geospatial Analysis

* `lab-jupyter-launch-site-location-v2.ipynb`: Visualizes launch sites using `Folium`.

  * Marker clustering
  * Distance calculations
  * Success/failure rates by site

### 🤖 Machine Learning

* `SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`: Predictive modeling using:

  * **Logistic Regression**
  * **SVM**
  * **KNN**
  * **Decision Trees**
  * Hyperparameter tuning & evaluation

### 📈 Interactive Dashboard

* `spacex_dash_app.py`: Dash app to explore launch data interactively.

---

## 🔧 Tech Stack

<a href="#"> 
  <img alt="Python" src="https://img.shields.io/badge/Python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white"/>
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white"/>
  <img alt="BeautifulSoup" src="https://img.shields.io/badge/BeautifulSoup-%23366088.svg?&style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?&style=for-the-badge&logo=matplotlib&logoColor=black"/>
  <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-%231572B6.svg?&style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Folium" src="https://img.shields.io/badge/Folium-%232C3E50.svg?&style=for-the-badge&logo=leaflet&logoColor=white"/>
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-%23003B57.svg?&style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img alt="Scikit-learn" src="https://img.shields.io/badge/Scikit--learn-%23F7931E.svg?&style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img alt="Dash" src="https://img.shields.io/badge/Dash-%2300171B.svg?&style=for-the-badge&logo=plotly&logoColor=white"/>
  <img alt="tqdm" src="https://img.shields.io/badge/tqdm-%23FFD700.svg?&style=for-the-badge&logo=python&logoColor=blue"/>
</a>

---

## 🚀 How to Use This Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/spacex-falcon9-analysis.git
   cd spacex-falcon9-analysis
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebooks in the order provided to follow the full pipeline.

4. Start the Dash application

   ```bash
   python spacex_dash_app.py
   ```

---

## 📌 Key Findings

* Launch success is highly correlated with **launch site**, **payload mass**, and **orbit type**.
* Machine learning models achieved good accuracy predicting first-stage landing success.
* Geospatial analysis revealed visual clusters of success/failure zones.

---

## 📈 Future Improvements

* Add more recent launch data via the SpaceX API.
* Engineer more complex features (weather, booster version, etc.).
* Explore advanced ML models like Gradient Boosting or Neural Nets.
* Expand dashboard features with filters, timelines, and real-time updates.

---

## 🔗 Live Demo

[🌐 View the deployed dashboard on Render](https://spacex-falcon9-landing-prediction-keoh.onrender.com/)

---

## 🙌 Credits

Developed as part of a Data Science course using IBM-provided datasets and labs.