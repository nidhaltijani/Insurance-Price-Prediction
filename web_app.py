import joblib 
import streamlit as st 
import sklearn
import pandas as pd


def main():
    st.title('Health insurance price prediction')
    model=joblib.load(open("insurance_model_final.pkl","rb"))
    age=st.slider("Age",0,100,18)
    gender = st.selectbox(label='Gender', options=['Male','Female'])
    if gender=='Male':
        gender=0
    elif gender=='Female':
        gender=1
    bmi=st.number_input("Enter your BMI")
    childrens=st.slider("Number of childrens",0,10,0)
    smoker = st.selectbox(label='Smoker', options=['Yes','No'])
    if smoker=='Yes':
        smoker=0
    elif smoker=='No':
        smoker=1
    region1=0
    region2=0
    region3=0
    region4=0
    region = st.selectbox(label='Region', options=['southwest', 'southeast', 'northwest', 'northeast'])
    if region =='southwest':
        region1=1
    elif region == 'southeast':
        region2=1
    elif region == 'northwest':
        region3=1
    elif region == 'northeast':
        region4=1
    
    df_pred = pd.DataFrame({'age' : age,
        'sex' : gender,
        'bmi' : bmi,
        'children' : childrens,
        'smoker' : smoker,
        'region_northeast':region1,
        'region_northwest' :region2,
        'region_southeast' :region3,
        'region_southwest':region4},index=[0])
    submitted=st.button("Submit")
    if submitted:
        prediction=model.predict(df_pred)
        st.success(f'your health insurance prediction is {prediction[0]}')
        
        
if __name__=='__main__':
    main()