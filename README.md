# Vaccine Usage Prediction & Zomato Data Analysis And Visualization
This repository contains both Vaccine Usage Prediction project and Zomato Data Analysis And Visualization project
</br>
</br>
</br>


# Project 1 - H1N1 Vaccine Prediction App

## Overview

The **H1N1 Vaccine Prediction App** is a web application designed to predict the likelihood of an individual taking the H1N1 flu vaccine based on their characteristics and attitudes. This information can be invaluable for public health officials and policymakers to effectively target vaccination campaigns.

## Features

- **Learn about H1N1**: Provides a brief overview of the H1N1 flu virus and the importance of vaccination.
- **Explore Data**: Discover trends and insights from the data used to build the prediction model with interactive charts and filters.
- **Predict Vaccine Usage**: Input your own answers to questions related to demographics, behaviors, and perceptions to get a prediction of your likelihood to take the H1N1 vaccine.
- **Understand the Model**: Learn more about the machine learning model used for prediction, including its limitations and development process.


## Usage

1. Learn about the H1N1 flu virus and the importance of vaccination.
2. Explore data trends and insights through interactive visualizations.
3. Input your demographic and behavioral data to predict your likelihood of taking the H1N1 vaccine.
4. Understand the machine learning model used for making predictions.

## Technologies Used

- **Streamlit**: For building the web application.
- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **Scikit-Learn**: Machine learning library for model building and evaluation.

## Data

The data used for training the machine learning model can be found [here](https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/Vaccine.csv). It includes demographic, behavioral, and attitudinal information relevant to H1N1 vaccination.

## Model

The prediction model is built using the **GradientBoostingClassifier** and trained on the provided dataset. The model's performance is evaluated using standard evaluation metrics.

## Limitations

- This app is for informational purposes only and should not be used as a substitute for professional medical advice.
- The data used to train the model may not be completely representative of the entire population.

---
</br>
</br>
</br>


# Project 2 - Zomato Data Analysis And Visualization

## Problem Statement
Zomato is a popular restaurant discovery and food delivery service. Data analysis on the platform's data could be used to gain insights into customer preferences and behavior, as well as identify trends in the restaurant industry. To perform the analysis, various methodologies such as Data Exploration, Data Cleaning, Feature Selection, and Deployment can be used. Additionally, various data visualization techniques like bar charts, line charts, scatter plots, etc., could be employed to help communicate the insights gained from the analysis. Overall, data visualization can be used to effectively communicate the insights from Zomato data analysis to a wide range of stakeholders, including restaurants, food industry players, and investors.

## Approach
You’ll be able to access the Zomato dataset and the country ISO code for all the countries in the dataset from the below URLs:
- [Zomato Dataset](https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv)
- [Country ISO Codes](https://github.com/nethajinirmal13/Training-datasets/blob/main/zomato/Country-Code.xlsx)

## TASK 1: DATA ENGINEERING
1. Add a column with rupees as the currency.
2. Bring out a plot that compares Indian currency with other country’s currency.

## TASK 2: DASHBOARD DEVELOPMENT
The Plotly or Streamlit Dashboard that is being developed is recommended to have the following:
- **Create a dropdown to choose the country-specific data**:
  - Any two charts of your choice (maybe count, total sales, favorite cuisines, etc).
- **Find which cuisines are costly in India**.
- **Filter based on the city**:
  - Which is the famous cuisine in the city.
  - Which is the costlier cuisine.
  - Rating count in the city (based on rating text).
  - Pie chart online delivery vs dine-in.
- **Comparison between the cities in India (own report)**:
  - Which part of India spends more on online delivery.
  - Which part of India spends more on dine-in.
  - Which part has a high living cost vs low living cost.

## Features
1. **Currency Conversion**: Add a column with costs converted to Indian Rupees (INR).
2. **Currency Comparison Plot**: Visualize a comparison of costs in Indian Rupees with other currencies.
3. **Interactive Dashboard**:
   - **Country-Specific Data**: A dropdown to select and view data specific to a country, along with two customizable charts (e.g., restaurant count, total sales, favorite cuisines).
   - **Costly Cuisines in India**: Identify which cuisines are the most expensive in India.
   - **City-Based Analysis**:
     - Identify the most famous cuisine in a city.
     - Determine the costliest cuisine in a city.
     - Analyze rating counts in the city based on rating texts.
     - Visualize the ratio of online delivery vs dine-in using a pie chart.
   - **Comparison Across Cities in India**:
     - Determine which part of India spends more on online delivery.
     - Determine which part of India spends more on dine-in.
     - Compare the living costs across different parts of India.

## Usage
1. **Currency Conversion and Comparison**:
   - Convert restaurant costs to Indian Rupees.
   - Compare restaurant costs in INR with other currencies using visual plots.
2. **Interactive Dashboard**:
   - Select a country from the dropdown to view specific data.
   - Use customizable charts to visualize different metrics.
   - Filter data based on city to find popular and expensive cuisines.
   - Analyze rating counts and delivery vs dine-in preferences using various visualizations.
   - Compare spending habits and living costs across different Indian cities.

## Technologies Used
- **Streamlit**: For building the interactive dashboard.
- **Plotly**: For creating dynamic and interactive visualizations.
- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **Jupyter Notebook**: For data exploration and prototyping.

## Data
The datasets used for this project can be found at:
- [Zomato Dataset](https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv)
- [Country ISO Codes](https://github.com/nethajinirmal13/Training-datasets/blob/main/zomato/Country-Code.xlsx)

## Limitations
- The analysis is based on the data available and may not be representative of all possible data.
- The insights gained should be used as a guideline and not as definitive facts.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
