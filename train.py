import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

dataFrame = pd.read_csv('data/Phishing_Email.csv')

dataFrame = dataFrame.dropna(subset=['Email Text'])
dataFrame = dataFrame[dataFrame['Email Text'].str.strip() != '']

# TRAIN / TEST
x = dataFrame['Email Text']
y = dataFrame['Email Type'].map({'Phishing Email': 1, 'Safe Email': 0})

# TF-IDF Vectorization
# On utilise X_train, X_test, y_train, y_test pour entraîner et tester le modèle.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Vectorisation des textes
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Entraînement du modèle
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Évaluation du modèle
y_pred = model.predict(X_test_vec)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["Safe", "Phishing"]))

# Sauvegarde du modèle et du vectorizer
joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")
print("Model and vectorizer saved successfully.")