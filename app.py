

import streamlit as st
import pandas as pd
import numpy as np
import pickle



from PIL import Image

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)


def welcome():
    return "welcome all"

def predict_note_authentications(age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar, restecg, max_hr, exang, oldpeak,slope, num_major_vessels, thal):
    
    age = float(age)
    sex = float(sex)  # Assuming sex is already encoded as numeric (e.g., Male: 1, Female: 0)
    chest_pain_type = float(chest_pain_type)
    resting_bp = float(resting_bp)
    cholestoral = float(cholestoral)
    fasting_blood_sugar = float(fasting_blood_sugar)
    restecg = float(restecg)
    max_hr = float(max_hr)
    exang = float(exang)
    oldpeak = float(oldpeak)
    slope = float(slope)
    num_major_vessels = float(num_major_vessels)
    thal = float(thal)
    
    
    prediction = classifier.predict([[age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar, restecg, max_hr, exang, oldpeak,slope, num_major_vessels, thal]])
    print(prediction)
    return prediction







def main():
    st.title("Heart disease prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart disease prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("age")
    sex = st.text_input("sex 1 for male and 0 for female")
    chest_pain_type = st.text_input("chest_pain_type")
    resting_bp = st.text_input("resting_bp")
    cholestoral = st.text_input("cholestoral")
    fasting_blood_sugar = st.text_input("fasting_blood_sugar 1 for true 0 for false")
    restecg = st.text_input("restecg (values 0,1,2)")
    max_hr = st.text_input("max_hr")
    exang = st.text_input("exang 0 for no 1 for yes")
    oldpeak = st.text_input("oldpeak")
    slope = st.text_input("slope")
    num_major_vessels = st.text_input("num_major_vessels")
    thal = st.text_input("thal 0 = normal; 1 = fixed defect; 2 = reversable defect")
    result = ""

 # Predict button
    if st.button("Predict"):
        st.text("[0] no disease, [1] have disease ")
        # Check if any input is empty
        if age == "" or sex == "" or chest_pain_type == "" or resting_bp == "" or cholestoral == "" or fasting_blood_sugar == "" or restecg == "" or max_hr == "" or exang == "" or oldpeak == "" or slope == "" or num_major_vessels == "" or thal == "":
            st.warning("Please fill in all the input fields.")
        else:
            result = predict_note_authentications(age, sex, chest_pain_type, resting_bp, cholestoral, fasting_blood_sugar, restecg, max_hr, exang, oldpeak, slope, num_major_vessels, thal)
            st.success("Prediction: {}".format(result))
    if st.button("About"):
        st.text("Developed by chahil choudhary")
        st.markdown("[Link to linkedin](https://www.linkedin.com/in/chahil-choudhary/)")


if __name__ =='__main__':
    main()