import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# Load pre-trained models
diabetes_model = pickle.load(open(r"C:\Users\User\Desktop\Disease prediction\saved_models\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\User\Desktop\Disease prediction\saved_models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\User\Desktop\Disease prediction\saved_models\parkinsons_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    Pregnancies = st.text_input('Number of Pregnancies (Integer) [Number of times the person has been pregnant.]')
    Glucose = st.text_input('Glucose Level (Integer) [Plasma glucose concentration at 2 hours in an oral glucose tolerance test.]')
    BloodPressure = st.text_input('Blood Pressure (Integer) [Diastolic blood pressure (mm Hg).]')
    SkinThickness = st.text_input('Skin Thickness (Integer) [Skin thickness measurement (mm).]')
    Insulin = st.text_input('Insulin Level (Integer) [2-Hour serum insulin (mu U/ml).]')
    BMI = st.text_input('BMI (Float) [Body mass index (kg/m^2).]')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function (Float) [A function which scores the likelihood of diabetes based on family history.]')
    Age = st.text_input('Age (Integer) [Age of the person.]')
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    Age = st.text_input('Age (Integer) [Age of the person.]')
    Sex = st.text_input('Sex (Integer) [Gender (1 for male, 0 for female).]')
    Cp = st.text_input('Chest Pain Type (Integer) [Type of chest pain (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic).]')
    Trestbps = st.text_input('Resting Blood Pressure (Integer) [Resting blood pressure (mm Hg).]')
    Chol = st.text_input('Cholesterol Level (Integer) [Serum cholesterol in mg/dl.]')
    Fbs = st.text_input('Fasting Blood Sugar (Integer) [Fasting blood sugar > 120 mg/dl (1: true, 0: false).]')
    Restecg = st.text_input('Resting Electrocardiographic Results (Integer) [Resting electrocardiographic results (0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy).]')
    Thalach = st.text_input('Max Heart Rate (Integer) [Maximum heart rate achieved.]')
    Exang = st.text_input('Exercise Induced Angina (Integer) [Exercise induced angina (1: yes, 0: no).]')
    Oldpeak = st.text_input('Oldpeak (Float) [Depression induced by exercise relative to rest.]')
    Slope = st.text_input('Slope (Integer) [Slope of the peak exercise ST segment.]')
    Ca = st.text_input('Number of Major Vessels (Integer) [Number of major vessels colored by fluoroscopy.]')
    Thal = st.text_input('Thalassemia (Integer) [Thalassemia (1: fixed defect, 2: normal, 3: reversible defect).]')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

elif selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction using ML')

    MDVP_Fo = st.text_input('MDVP:Fo (Hz) (Float) [Fundamental frequency (Hz).]')
    MDVP_Fhi = st.text_input('MDVP:Fhi (Hz) (Float) [Highest fundamental frequency (Hz).]')
    MDVP_Flo = st.text_input('MDVP:Flo (Hz) (Float) [Lowest fundamental frequency (Hz).]')
    MDVP_Jitter = st.text_input('MDVP:Jitter (%) (Float) [Percentage of jitter in the speech signal.]')
    MDVP_JitterAbs = st.text_input('MDVP:Jitter (Abs) (Float) [Absolute jitter in the speech signal.]')
    MDVP_RAP = st.text_input('MDVP:RAP (Float) [Relative Average Perturbation.]')
    MDVP_PPQ = st.text_input('MDVP:PPQ (Float) [Pitch Period Quotient.]')
    
    park_diagnosis = ''
    if st.button('Parkinson’s Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_JitterAbs, MDVP_RAP, MDVP_PPQ]
        user_input = [float(x) for x in user_input]
        park_prediction = parkinsons_model.predict([user_input])
        if park_prediction[0] == 1:
            park_diagnosis = 'The person has Parkinson’s disease'
        else:
            park_diagnosis = 'The person does not have Parkinson’s disease'
    st.success(park_diagnosis)
