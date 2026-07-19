# Phishing Email Detector

Petit projet Data / IA + cybersécurité : classer un mail en **Safe** ou **Phishing** avec du Machine Learning classique (TF-IDF + Logistic Regression).

## Démo

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pandas scikit-learn joblib streamlit
python train.py
streamlit run app.py

Dataset
Phishing Email Dataset (Kaggle)

Colonnes utilisées : Email Text, Email Type (Safe Email / Phishing Email).

Place le CSV dans data/Phishing_Email.csv avant d'entraîner.

Approche
Nettoyage des mails vides
Split train/test (80/20, stratifié)
Vectorisation TF-IDF (texte → nombres)
Classification avec Logistic Regression
Interface Streamlit (prédiction + proba)
Résultats (test set)
Accuracy ≈ 96 %
Phishing recall ≈ 97 %
Safe F1 ≈ 0.97 / Phishing F1 ≈ 0.95
Stack
Python · pandas · scikit-learn · joblib · Streamlit

Limites
Dataset surtout en anglais
Pas d'analyse avancée des URLs / pièces jointes
Modèle classique (pas un LLM) : choix volontaire pour un socle Data Science solide
Auteure
Sokhna Ndione — Bachelor Full-Stack Big Data & IA (ESGI)
