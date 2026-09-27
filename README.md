# Crop Suitability Classification

## 1. Project Overview

This project develops a machine learning based crop suitability prediction system.

The system uses soil and weather-related parameters to predict a suitable crop. The project includes data analysis, preprocessing, model training, model comparison, evaluation, and a Streamlit-based prototype.

## 2. Problem Statement

Selecting a suitable crop depends on several environmental and soil conditions. This project uses machine learning to classify a suitable crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

## 3. Dataset

The project uses a public Crop Recommendation dataset.

The dataset contains 2,200 records and 8 columns.

### Features

- N
- P
- K
- temperature
- humidity
- ph
- rainfall

### Target

- label

The `label` column represents the crop class to be predicted.

## 4. Machine Learning Workflow

The project follows these steps:

1. Load the dataset
2. Inspect the data
3. Check missing values and duplicates
4. Perform exploratory data analysis
5. Separate features and target
6. Split the data into training and testing sets
7. Train multiple classification models
8. Compare model performance
9. Perform 5-fold cross-validation
10. Select the final model
11. Evaluate the selected model
12. Save the trained model
13. Build a Streamlit prototype

## 5. Models Used

Three classification algorithms were evaluated:

### Logistic Regression

Used as a baseline classification model.

### Decision Tree

Used to model non-linear relationships between the input features and crop classes.

### Random Forest

An ensemble model consisting of multiple decision trees.

## 6. Model Selection

The models were compared using 5-fold cross-validation.

| Model | Mean Accuracy | Standard Deviation |
|---|---:|---:|
| Logistic Regression | 0.9709 | 0.0058 |
| Decision Tree | 0.9868 | 0.0033 |
| Random Forest | 0.9945 | 0.0023 |

Based on the cross-validation results, Random Forest was selected as the final model for the prototype.

## 7. Evaluation Metrics

The final model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics provide a more detailed view of classification performance.

## 8. Streamlit Prototype

A Streamlit application was developed to provide a simple user interface.

The user enters:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Soil pH
- Rainfall

The saved Random Forest model processes the inputs and predicts a suitable crop.

## 9. Project Structure

```text
crop-selection-project-learn-depth/
│
├── app.py
├── Crop_recommendation.csv
├── crop_recommendation_model.pkl
├── requirements.txt
└── README.md