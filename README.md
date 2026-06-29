# ❤️ Heart Disease Prediction Portal

A machine learning web application built with Streamlit that predicts the risk of heart disease based on medical parameters and patient health data.

## Overview

The **Heart Disease Prediction Portal** is an interactive web application that uses a K-Nearest Neighbors (KNN) machine learning model to predict the likelihood of heart disease in patients. Users input their medical information, and the application provides a prediction along with risk assessment.

### Key Objectives:
- Provide quick heart disease risk assessment
- Help users understand their health metrics
- Use machine learning for data-driven predictions
- Offer an intuitive, user-friendly interface

## Features

- **Interactive User Interface**: Built with Streamlit for an easy-to-use web experience
- **Real-time Predictions**: Instant heart disease risk assessment
- **Comprehensive Input Form**: Collects all relevant medical parameters
- **Risk Classification**: Clear categorization as HIGH RISK or LOW RISK
- **Input Preprocessing**: Automatic one-hot encoding and feature scaling
- **Data Validation**: Ensures input data aligns with training data structure
- **Visual Feedback**: Color-coded results (red for high risk, green for low risk)
- **Input Summary**: Expandable section showing processed features

##  Project Structure

```
Heart/
├── app.py                          # Main Streamlit application
├── HeartDisease.ipynb              # Jupyter notebook with model development
├── HeartDisease-checkpoint.ipynb   # Backup checkpoint of notebook
├── heart.csv                       # Original raw dataset
├── heart_preprocessed.csv          # Preprocessed dataset
├── heart-checkpoint.csv            # Backup of preprocessed data
├── knn_heart_model.pkl             # Trained KNN model (binary)
├── scaler.pkl                      # Fitted StandardScaler for normalization
├── columns.pkl                     # Expected column names after encoding
└── README.md                       # This file
```

##  Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory**:
   ```bash
   cd Heart
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On macOS/Linux
   ```

3. **Install required packages**:
   ```bash
   pip install streamlit pandas joblib scikit-learn
   ```

   Or install from a requirements file (if available):
   ```bash
   pip install -r requirements.txt
   ```

##  Usage

### Running the Application

1. **Start the Streamlit server**:
   ```bash
   streamlit run app.py
   ```

2. **Open in browser**: The application will automatically open at `http://localhost:8501`

3. **Enter medical information**: Fill out the form with patient details

4. **Click "Predict"**: Get instant heart disease risk assessment

### Example Workflow

1. Adjust Age slider to patient's age
2. Select biological Sex (Male/Female)
3. Choose Chest Pain Type from dropdown
4. Enter Resting Blood Pressure in mmHg
5. Input Cholesterol level in mg/dL
6. Specify Fasting Blood Sugar status
7. Select Resting ECG result
8. Set Max Heart Rate Achieved
9. Indicate if Exercise-Induced Angina occurs
10. Enter Oldpeak (ST Depression) value
11. Choose ST Slope type
12. Click "🔍 Predict" button
13. View results and input summary

## Input Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| **Age** | Slider | 18-100 years | Patient's age in years |
| **Sex** | Dropdown | Male, Female | Biological sex of patient |
| **Chest Pain Type** | Dropdown | ATA, NAP, ASY, TA | Type of chest pain experienced |
| **Resting BP** | Number | 80-200 mmHg | Resting blood pressure |
| **Cholesterol** | Number | 100-600 mg/dL | Total cholesterol level |
| **Fasting BS** | Dropdown | 0, 1 | Fasting blood sugar > 120 mg/dL (0=No, 1=Yes) |
| **Resting ECG** | Dropdown | Normal, ST, LVH | Resting electrocardiogram result |
| **Max HR** | Slider | 60-220 bpm | Maximum heart rate achieved during exercise |
| **Exercise Angina** | Dropdown | Yes, No | Exercise-induced chest pain presence |
| **Oldpeak** | Number | 0.0-6.0 | ST depression induced by exercise relative to rest |
| **ST Slope** | Dropdown | Up, Flat, Down | Slope of the ST segment of the ECG |

### Chest Pain Types
- **ASY**: Asymptomatic (no chest pain)
- **ATA**: Atypical Angina
- **NAP**: Non-anginal Pain
- **TA**: Typical Angina

### Resting ECG Types
- **Normal**: Normal electrocardiogram
- **ST**: ST-T wave abnormality
- **LVH**: Left ventricular hypertrophy

##  Model Details

### Algorithm
- **Type**: K-Nearest Neighbors (KNN) Classifier
- **Task**: Binary Classification (Heart Disease Present/Absent)
- **Output**: 
  - `1` = HIGH RISK - Heart Disease likely present
  - `0` = LOW RISK - Heart Disease unlikely

### Data Preprocessing
1. **One-Hot Encoding**: Categorical features are encoded:
   - Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope
2. **Feature Scaling**: StandardScaler normalizes numerical features
3. **Column Alignment**: Input features are aligned with training data structure

### Model Files
- `knn_heart_model.pkl`: Serialized trained KNN classifier
- `scaler.pkl`: Fitted scaler for feature normalization
- `columns.pkl`: Expected column names after one-hot encoding

##  Data Files

### Original Data
- **heart.csv**: Raw dataset with original heart disease data
- Format: CSV with patient records and diagnosis outcomes

### Preprocessed Data
- **heart_preprocessed.csv**: Cleaned and processed dataset ready for modeling
- **heart-checkpoint.csv**: Backup of preprocessed data

### Notebooks
- **HeartDisease.ipynb**: Jupyter notebook containing:
  - Exploratory Data Analysis (EDA)
  - Data preprocessing pipeline
  - Model training and evaluation
  - Feature engineering steps
- **HeartDisease-checkpoint.ipynb**: Checkpoint version for backup

##  Technical Stack

### Libraries & Frameworks
- **Streamlit**: Web application framework for interactive ML apps
- **Pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning library (KNN, preprocessing)
- **joblib**: Model serialization and deserialization

### Python Version
- Python 3.7+

### Development Tools
- Jupyter Notebook (for model development)
- Git (for version control)

##  Application Flow

```
User Input
    ↓
Create DataFrame
    ↓
One-Hot Encode Categorical Features
    ↓
Align Columns with Expected Features
    ↓
Scale Features Using StandardScaler
    ↓
KNN Model Prediction
    ↓
Risk Assessment (HIGH/LOW)
    ↓
Display Results & Input Summary
```

##  Output Interpretation

### HIGH RISK Result
- High likelihood of heart disease
- Recommendation: Consult a cardiologist immediately
- Consider diagnostic tests and medical evaluation

### LOW RISK Result
- Low likelihood of heart disease
- Recommendation: Maintain healthy lifestyle
- Continue regular health check-ups


