import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_prediction_model.pkl")

st.set_page_config(page_title="💼 Employee Salary Predictor", page_icon="💰", layout="centered")
st.sidebar.title("📊 Navigation")
st.sidebar.info("Fill out employee details and click Predict.")
st.sidebar.success("Made by Gagana 🚀")
st.sidebar.markdown("💻 IBM-AICTE Internship Project")
st.title("💼 Employee Salary Prediction App")
st.markdown("Use this tool to estimate monthly salary based on job details.")

age = st.slider("Age", 21, 60, 25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
job_role = st.selectbox("Job Role", ["Developer", "Manager", "Analyst", "HR", "Designer", "Tester",
                                     "Tech Lead", "Data Scientist", "System Admin", "Consultant"])
experience = st.slider("Years of Experience", 0, 40, 2)
city = st.selectbox("City", ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad', 'Pune',
                             'Kolkata', 'Ahmedabad', 'Jaipur', 'Kochi'])
company_type = st.selectbox("Company Type", ['Startup', 'MNC', 'Government', 'Mid-size',
                                             'Consultancy', 'NGO', 'Product-Based'])
work_hours = st.slider("Work Hours per Week", 30, 60, 40)

if st.button("🎯 Predict Salary"):
    input_df = pd.DataFrame([{
        'Age': age,
        'Gender': gender,
        'Education': education,
        'JobRole': job_role,
        'Experience': experience,
        'City': city,
        'CompanyType': company_type,
        'WorkHours': work_hours
    }])
    prediction = model.predict(input_df)[0]
    st.success(f"✅ Estimated Monthly Salary: ₹{int(prediction):,}")
    st.markdown("Note: This is an estimate based on the trained data.")
st.markdown("---")
st.caption("© 2025 Gagana | IBM-AICTE Internship Project")
