
import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('C:/Users/Krish Solanki/OneDrive/intership/placement/placement_model.sav', 'rb'))

# Prediction function
def salary_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return round(prediction[0], 2)

# Main UI
def main():
    st.set_page_config(page_title="Salary Prediction", page_icon="💼")
    st.title('💼 Salary Prediction Web App')
    st.markdown("##### Fill the student’s academic and profile details to predict expected salary.")

    col1, col2 = st.columns(2)

    with col1:
        ssc_p = st.text_input('📘 SSC Percentage')
        hsc_p = st.text_input('📗 HSC Percentage')
        hsc_s = st.selectbox('📚 HSC Stream', ['Commerce', 'Science', 'Arts'])
        degree_p = st.text_input('🎓 Degree Percentage')
        degree_t = st.selectbox('🏫 Degree Type', ['Sci&Tech', 'Comm&Mgmt', 'Others'])

    with col2:
        workex = st.selectbox('💼 Work Experience', ['Yes', 'No'])
        etest_p = st.text_input('🧠 E-test Score Percentage')
        specialisation = st.selectbox('📈 MBA Specialisation', ['Mkt&Fin', 'Mkt&HR'])
        mba_p = st.text_input('📊 MBA Percentage')
        status = st.selectbox('🎯 Placement Status', ['Placed', 'Not Placed'])

    result = ''
    if st.button('🔍 Predict Salary'):
        try:
            # Encode categorical fields
            hsc_s_encoded = {'Commerce': 0, 'Science': 1, 'Arts': 2}[hsc_s]
            degree_t_encoded = {'Sci&Tech': 0, 'Comm&Mgmt': 1, 'Others': 2}[degree_t]
            workex_encoded = {'No': 0, 'Yes': 1}[workex]
            specialisation_encoded = {'Mkt&Fin': 0, 'Mkt&HR': 1}[specialisation]
            status_encoded = {'Not Placed': 0, 'Placed': 1}[status]

            # Input list for model
            input_list = [
                float(ssc_p), float(hsc_p), hsc_s_encoded,
                float(degree_p), degree_t_encoded, workex_encoded,
                float(etest_p), specialisation_encoded, float(mba_p),
                status_encoded
            ]

            salary = salary_prediction(input_list)
            result = f"💰 Predicted Salary: ₹{salary:.2f}"

        except ValueError:
            result = "⚠️ Please enter valid numbers for all percentage fields."

    st.success(result)

if __name__ == '__main__':
    main()
