from prediction import predict_class
import streamlit as st
st.header("Diabetic Prediction")
input_data = {}
with st.form("my_form"):
    gender = st.radio("Gender", ('M', 'F'))
    age = st.number_input("Age", min_value=0)
    urea = st.number_input("Urea", min_value=0.0)
    cr = st.number_input("Creatinine", min_value=0.0)
    hba1c = st.number_input("HbA1c", min_value=0.0)
    chol = st.number_input("Cholesterol", min_value=0.0)
    tg = st.number_input("Triglycerides", min_value=0.0)
    hdl = st.number_input("HDL", min_value=0.0)
    ldl = st.number_input("LDL", min_value=0.0)
    vldl = st.number_input("VLDL", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        input_data = {
            'Gender': gender,
            'AGE': float(age),
            'Urea': float(urea),
            'Cr': float(cr),
            'HbA1c': float(hba1c),
            'Chol': float(chol),
            'TG': float(tg),
            'HDL': float(hdl),
            'LDL': float(ldl),
            'VLDL': float(vldl),
            'BMI': float(bmi)
        }
st.write("Outside the form")
if input_data:
    y = predict_class(input_data)
    if y=='Negative':
        # show text in red
        st.markdown(f"<h5 style='color:red;'>Result: {y}</h5>", unsafe_allow_html=True)
    elif y=='Suspect':
        # show text in orange
        st.markdown(f"<h5 style='color:orange;'>Result: {y}</h5>", unsafe_allow_html=True)
    elif y=='Positive':
        # show text in green
        st.markdown(f"<h5 style='color:green;'>Result: {y}</h5>", unsafe_allow_html=True)