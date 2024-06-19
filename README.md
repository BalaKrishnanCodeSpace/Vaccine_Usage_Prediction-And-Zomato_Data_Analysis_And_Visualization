# Vaccine Usage Prediction & GitHub User Analytics and Recommendation
This repository contains both Vaccine Usage Prediction project and GitHub User Analytics Recommendation project

# H1N1 Vaccine Prediction App

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
