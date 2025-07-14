# SpaceX Falcon 9 Launch Analysis Project

## Project Overview
This project analyzes SpaceX Falcon 9 rocket launches to predict first-stage landing success. By determining landing outcome predictability, we can estimate the cost of a launch. SpaceX advertises Falcon 9 rocket launches at $62 million, significantly less than other providers (which cost upward of $165 million) primarily because SpaceX can reuse the first stage.

## Repository Contents

### Data Collection
- `jupyter-labs-webscraping.ipynb`: Extracts Falcon 9 launch records from Wikipedia using BeautifulSoup
- `jupyter-labs-spacex-data-collection-api-v2.ipynb`: Collects detailed launch data using SpaceX REST API

### Data Processing
- `labs-jupyter-spacex-Data wrangling-v2.ipynb`: Cleans and prepares data for analysis

### Exploratory Data Analysis (EDA)
- `jupyter-labs-eda-sql-coursera_sqllite.ipynb`: SQL-based data exploration
- `jupyter-labs-eda-dataviz-v2.ipynb`: Data visualization and pattern discovery

### Geospatial Analysis
- `lab-jupyter-launch-site-location-v2.ipynb`: Maps and analyzes launch sites with Folium
  - Visualizes launch success/failure rates by location
  - Calculates distances to key facilities
  - Uses marker clustering to identify patterns

### Machine Learning
- `SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`: Builds predictive models
  - Applies SVM, Decision Trees, Logistic Regression, and KNN
  - Performs hyperparameter tuning
  - Evaluates model performance

### Interactive Dashboard
- `spacex_dash_app.py`: A Dash application that provides interactive visualization of launch data

## Technologies Used
- **Python**: Primary programming language
- **Pandas & NumPy**: Data manipulation
- **BeautifulSoup**: Web scraping
- **Requests**: API interaction
- **Matplotlib & Seaborn**: Data visualization
- **Folium**: Geospatial mapping
- **SQLite**: Database operations
- **Scikit-learn**: Machine learning
- **Dash**: Interactive dashboard

## How to Use This Project
- Install required libraries using:  
  `pip install -r requirements.txt`
- Follow the notebooks in the order listed above for a complete data science workflow
- Each notebook contains detailed markdown explaining the purpose and methods used
- Run the Dash application to interact with the data visualizations: `python spacex_dash_app.py`

## Key Findings
- Launch success rates vary significantly by launch site
- Several factors correlate with successful landings, including payload mass and orbit type
- Machine learning models can predict landing success with good accuracy

## Future Work
- Incorporate more recent launch data
- Explore additional features that might affect landing success
- Develop more sophisticated machine learning models
- Expand the dashboard functionality

## Live Demo

[View the deployed SpaceX Launch Dashboard](https://spacex-falcon9-landing-prediction-ahnx.onrender.com)

## Credits
This project was developed as part of a data science course with materials from IBM.
