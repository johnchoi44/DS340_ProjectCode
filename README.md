<h1 align="center">
  <br>
  End-to-End New York City Crimes Detection using Machine Learning


</h1>

<div align="center">
  <h4>
    <a href="#Overview">Overview</a> |
    <a href="#dataset">Dataset</a> |
    <a href="#notebooks">Notebooks</a> |
    <a href="#technologies">Technologies</a> |
    <a href="#paper">Paper</a>
  </h4>
</div>

<br>

## Overview
A simple web application to predict crime probability in New York City depending on user information, location and time.
## Dataset

This work relies on [NYPD Complaint Data Historic Dataset](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i). This dataset includes all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) from 2006 to 2019. The dataset contains 6901167 complaints and 35 columns including spatial and temporal information about crime occurrences along with their description and penal classification.

## Notebooks

Different notebooks are provided for :
- [Data cleaning](https://github.com/mohamedkaraa/New-York-Crime-Prediction/blob/main/notebooks/ny_crimes_process.ipynb)
- [Exploratory Data Analysis](https://github.com/mohamedkaraa/New-York-Crime-Prediction/blob/main/notebooks/ny_crimes_eda.ipynb)
- [Modeling](https://github.com/mohamedkaraa/New-York-Crime-Prediction/blob/main/notebooks/ny_crimes_predict.ipynb)

## Technologies

This web application is developd using:
- Streamlit
- Folium

For data cleaning, EDA and modeling:
- Pandas
- seaborn
- matplotlib
- Scikit-learn
- lightgbm

To install requirements run:
```sh
pip install -r requirements.txt
```
## Paper

To document our work, we wrote a research paper that is included in the [repo](https://github.com/mohamedkaraa/New-York-Crime-Prediction/blob/main/docs/ny_crime_prediction_paper.pdf).