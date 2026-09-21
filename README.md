# Data Analysis Project 

## Overview
This project analyzes the Bike Sharing Dataset to identify patterns and trends in bike rental demand. The analysis covers data wrangling, exploratory data analysis (EDA), data visualization, and the development of an interactive dashboard to communicate the findings.

## Objectives
The project aims to:

- Explore patterns in bike rental usage.
- Analyze how factors such as season, weather, and time influence rental demand.
- Identify trends and differences in bike-sharing usage.
- Present the analysis results through interactive visualizations.

## Analysis Process

### 1. Data Wrangling
- Loaded and inspected the dataset.
- Checked data types and missing values.
- Cleaned and prepared the data for analysis.
- Created additional features where necessary.

### 2. Exploratory Data Analysis
- Examined the distribution of bike rentals.
- Analyzed rental patterns across different time periods.
- Investigated relationships between rental demand and environmental or seasonal factors.

### 3. Data Visualization
- Created visualizations to identify trends and relationships in the dataset.
- Used charts to make the analysis and findings easier to interpret.

### 4. Interactive Dashboard
- Developed an interactive dashboard using Streamlit.
- Added filters and visualizations to allow users to explore the dataset and analysis results interactively.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit

## Project Structure

```text
Proyek-Analisis-Data/
├── dashboard/
│   └── dashboard.py
├── data/
│   └── ...
├── notebook.ipynb
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anindyazlv/Proyek-Analisis-Data.git
cd Proyek-Analisis-Data
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

Open `notebook.ipynb` using Jupyter Notebook or JupyterLab.

### 4. Run the dashboard

```bash
streamlit run dashboard/dashboard.py
```

The dashboard will then be available through the local Streamlit server.
