import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(
    open('D:/Multiple Disease Prediction system/trained models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(
    open('D:/Multiple Disease Prediction system/trained models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(
    open('D:/Multiple Disease Prediction system/trained models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(
    open('D:/Multiple Disease Prediction system/trained models/breast_cancer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu(' Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           icons=['activity', 'heart', 'person', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'+ 'ㅤPercentage of Chance->'+str(diab_prediction[0]*100) + '%ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRefering to visit Doctor: Apollo Hospital,MaduraiㅤDr.PG Raman MBBS,MD Internal Medicane-Diabetology'

        else:
            diab_diagnosis = 'The person is not diabeticㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤStay classy Eat well. Live longer'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('cp')

    with col1:
        trestbps = st.text_input('trestbps')

    with col2:
        chol = st.text_input('chol')

    with col3:
        fbs = st.text_input('fbs')

    with col1:
        restecg = st.text_input('restecg')

    with col2:
        thalach = st.text_input('thalach')

    with col3:
        exang = st.text_input('exang')

    with col1:
        oldpeak = st.text_input('oldpeak')

    with col2:
        slope = st.text_input('slope')

    with col3:
        ca = st.text_input('ca')

    with col1:
        thal = st.text_input('thal')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having a chance to heart diseaseㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRefering to : DR. S. SELVAMANI, MBBS, DNB - MEENAKSHI MISSION HOSPITAL & RESEARCH CENTRE'
        else:
            heart_diagnosis = 'The person does not have any heart diseaseㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤStay classy Eat well. Live longer'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's diseaseㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRefering to : DR. C. Justin, MBBS, MD,ㅤㅤ DM Vadamalayan HospitalsㅤㅤMadurai"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's diseaseㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤStay classy Eat well. Live longe"

    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediction"):

    # page title
    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        radius_mean = st.text_input('radius_mean')

    with col2:
        texture_mean = st.text_input('texture_mean')

    with col3:
        perimeter_mean = st.text_input('perimeter_mean')

    with col4:
        area_mean = st.text_input('area_mean')

    with col5:
        smoothness_mean = st.text_input('smoothness_mean')

    with col1:
        compactness_mean = st.text_input('compactness_mean')

    with col2:
        concavity_mean = st.text_input('concavity_mean')

    with col3:
        concave_points_mean = st.text_input('concave points_mean')

    with col4:
        symmetry_mean = st.text_input('symmetry_mean')

    with col5:
        fractal_dimension_mean = st.text_input('fractal_dimension_mean')

    with col1:
        radius_se = st.text_input('radius_se')

    with col2:
        texture_se = st.text_input('texture_se')

    with col3:
        perimeter_se = st.text_input('perimeter_se')

    with col4:
        area_se = st.text_input('area_se')

    with col5:
        smoothness_se = st.text_input('smoothness_se')

    with col1:
        compactness_se = st.text_input('compactness_se')

    with col2:
        concavity_se = st.text_input('concavity_se')

    with col3:
        concave_points_se = st.text_input('concave points_se')

    with col4:
        symmetry_se = st.text_input('symmetry_se')

    with col5:
        fractal_dimension_se = st.text_input('fractal_dimension_se')

    with col1:
        radius_worst = st.text_input('radius_worst')

    with col2:
        texture_worst = st.text_input('texture_worst')

    with col3:
        perimeter_worst = st.text_input('perimeter_worst')

    with col4:
        area_worst = st.text_input('area_worst')


    # code for Prediction
    breast_cancer_diagnosis = ''

    # creating a button for Prediction
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                                                           compactness_mean, concavity_mean, concave_points_mean,
                                                           symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se,
                                                           area_se, smoothness_se, compactness_se, concavity_se,
                                                           concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst]])

        if (breast_cancer_prediction[0] == 1):
            breast_cancer_diagnosis = "The person has a chance to Breast CancerㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRefering to : DR. S.G. BALAMURAGAN  MS M.CH(oncology)- Guru Hospitals - Madurai"
        else:
            breast_cancer_diagnosis = "The person does not have Breast CancerㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤStay classy Eat well. Live longe"

    st.success(breast_cancer_diagnosis)
