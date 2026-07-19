import streamlit as st
import joblib

# Charger le modèle et le vectorizer
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Titre de l'application
st.title("Phishing Email Detector")
st.write("Enter the email text below to check if it's a phishing email or a safe email.")

# Champ de saisie pour le texte de l'email + bouton de prédiction
email_text = st.text_area("Email Text", height=200)
if st.button("Predict"):
    if email_text.strip() == "":
        st.warning("Please enter the email text.")
    else:
        # Vectorisation de texte et prédiction
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)[0]
        prediction_proba = model.predict_proba(email_vector)[0]

        if prediction == 1:
            st.error(f"This email is predicted to be a **Phishing Email** with a probability of {prediction_proba[1]:.2f}.")
        else:
            st.success(f"This email is predicted to be a **Safe Email** with a probability of {prediction_proba[0]:.2f}.")