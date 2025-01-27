import streamlit as st

st.title("Fever Detection App")
st.write("This app predicts if a patient has a fever based on symptoms provided.")

# Simplified prediction function using keyword matching
def predict(text):
    # Keywords commonly associated with fever
    fever_keywords = ["fever", "high temperature", "chills", "sweating", "shivering", "hot"]

    # Check for keywords in the input text
    text_lower = text.lower()
    fever_detected = any(keyword in text_lower for keyword in fever_keywords)

    # Define diagnosis and recommended medication
    diagnosis = "Fever detected" if fever_detected else "No fever"
    medication = {
        "Fever detected": "Paracetamol",
        "No fever": "Rest and hydration"
    }

    # Mock probabilities for demonstration purposes
    prob_no_fever = 0.2 if fever_detected else 0.8
    prob_fever = 0.8 if fever_detected else 0.2

    return diagnosis, medication[diagnosis], prob_no_fever, prob_fever

# User input section
st.subheader("Enter Symptoms")
input_text = st.text_area("Describe the symptoms below:")

if st.button("Predict"):
    if input_text.strip():  # Ensure input is not empty
        # Get prediction
        diagnosis, recommended_medication, prob_no_fever, prob_fever = predict(input_text)

        # Display results
        st.write(f"### Prediction: {diagnosis}")
        st.write(f"**Recommended Medication**: {recommended_medication}")
    else:
        st.warning("Please enter a description of the symptoms.")
