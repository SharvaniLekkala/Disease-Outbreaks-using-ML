# Disease Outbreak Prediction Using Machine Learning

## Overview

This project aims to predict the likelihood of diseases such as Diabetes, Heart Disease, and Parkinson's Disease using Machine Learning (ML) models. The web-based application, developed using **Streamlit**, allows users to input relevant medical parameters and receive instant predictions.

## Repository Structure

```
📂 Disease-Outbreak-Prediction
│-- 📂 DATASETS
│   │-- diabetes.csv
│   │-- heart.csv
│   │-- parkinsons.csv
│-- 📂 saved_models
│   │-- diabetes_model.sav
│   │-- heart_model.sav
│   │-- parkinsons_model.sav
│-- 📂 training_models
│   │-- diabetes.py
│   │-- heart.py
│   │-- parkinsons.py
│-- requirements.txt
│-- web.py
```

## Features

- **Machine Learning Models**: Uses **SVM (Support Vector Machine)** for classification.
- **Web Interface**: Built using **Streamlit** for easy interaction.
- **Multiple Disease Predictions**:
  - **Diabetes** (PIMA Indian Diabetes dataset)
  - **Heart Disease** (Cleveland Heart Disease dataset)
  - **Parkinson’s Disease** (UCI Machine Learning Repository dataset)

## Installation

### Prerequisites

Ensure you have **Python 3.7+** installed.

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training the Models

Navigate to the `training_models` directory and run each Python file to train models:

```bash
python diabetes.py
python heart.py
python parkinsons.py
```

This generates `.sav` files inside the `saved_models` directory.

Running the Web Application

To launch the web application, open a terminal or command prompt, navigate to the project directory, and run:

streamlit run web.py

This command starts a local web server and opens the application in a browser, where users can interact with the disease prediction system.

This will open a browser where users can interact with the disease prediction system.

## Usage

1. **Select a disease from the sidebar** (Diabetes, Heart Disease, or Parkinson’s).
2. **Enter the required medical parameters**.
3. **Click the "Test Result" button**.
4. **Receive the prediction** (either positive or negative for the disease).

## Dependencies

- `streamlit`
- `transformers`
- `tensorflow`
- `nltk`
- `tf-keras`
- `numpy`
- `pandas`
- `scikit-learn`
- `pickle`

## Screenshot
![image](https://github.com/user-attachments/assets/4b1f50eb-defc-477f-a839-98fbaa0f994c)

## Author

Sharvani - AI & Data Science Enthusiast

---

