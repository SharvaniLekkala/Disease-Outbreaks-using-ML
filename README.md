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
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Disease-Outbreak-Prediction.git
   cd Disease-Outbreak-Prediction
   ```
2. Install dependencies:
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

## Running the Web Application
Start the Streamlit application using:
```bash
streamlit run web.py
```
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

## Future Improvements
- Incorporate deep learning models for better accuracy.
- Enhance the UI with additional features.
- Include more disease predictions.

## License
This project is open-source and available under the MIT License.

## Author
[Your Name] - AI & Data Science Enthusiast

---
Feel free to contribute or raise issues!

