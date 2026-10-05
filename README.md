# Alzheimer's Disease Risk Prediction Using Machine Learning

## Overview

This project develops a machine-learning-based system for classifying dementia status using demographic, cognitive, and anatomical brain measurements.

The final model is an XGBoost classifier, with a Streamlit interface for making predictions.

> Disclaimer: This project is intended for educational and research purposes only. It is not a medical diagnostic system and should not be used for clinical decision-making.

## Objective

The objective is to classify patients into:

- NonDemented
- Demented

using demographic, cognitive, and anatomical features.

## Features

The final model uses:

- Age
- M/F
- Educ
- SES
- MMSE
- eTIV
- nWBV
- ASF

## Models Evaluated

The following models were evaluated:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

XGBoost was selected as the final model.

## Cross-Validation Performance

The final XGBoost model achieved the following 5-fold cross-validation results:

| Metric | Mean | Standard Deviation |
|---|---:|---:|
| Accuracy | 91.63% | 4.50% |
| Precision | 89.13% | 6.08% |
| Recall | 88.67% | 9.73% |
| F1 Score | 88.57% | 6.55% |
| ROC-AUC | 96.48% | 2.04% |

## Independent Test Performance

| Metric | Score |
|---|---:|
| Accuracy | 89.75% |
| Precision | 54.76% |
| Recall | 79.31% |
| F1 Score | 64.79% |
| ROC-AUC | 95.40% |

### Test Confusion Matrix

    [[196, 19],
     [  6, 23]]

Where:

- True Negatives = 196
- False Positives = 19
- False Negatives = 6
- True Positives = 23

## Explainable AI

SHAP was used to explain model predictions.

The analysis includes:

- Global feature importance
- SHAP summary plot
- Individual prediction explanations

## Streamlit Application

The Streamlit application allows users to enter patient information and receive:

- Predicted dementia status
- Estimated dementia probability

## Project Structure

    alzheimers_risk_prediction/
    |
    |-- app.py
    |-- alzheimers_xgboost_model.pkl
    |-- requirements.txt
    |-- README.md

## Installation

Clone the repository:

    git clone <your-github-repository-url>
    cd alzheimers_risk_prediction

Install dependencies:

    pip install -r requirements.txt

## Run the Application

    streamlit run app.py

## Machine Learning Workflow

    Dataset
       |
    Data Cleaning
       |
    Feature Selection
       |
    Missing Value Handling
       |
    Feature Encoding
       |
    Model Comparison
       |
    XGBoost Selection
       |
    Cross-Validation
       |
    SHAP Explainability
       |
    Final Model Training
       |
    Streamlit Application

## Limitations

- The dataset is relatively small.
- The independent test set has a different class distribution from the training data.
- The model is not a clinical diagnostic tool.
- Performance may not generalize to other populations or clinical settings.
- The predicted probability is a model output and should not be interpreted as a medical risk probability.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Joblib

## License

This project is intended for educational and research purposes.
