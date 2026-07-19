import pandas as pd;



dataFrame = pd.read_csv('data/Phishing_Email.csv')
print(dataFrame.shape)
print(dataFrame.columns.tolist())
print(dataFrame.head())
print(dataFrame.info())
print(dataFrame['Email Type'].value_counts())

print(dataFrame[dataFrame["Email Type"] == "Phishing Email"]["Email Text"].iloc[0][:300])
print("---")
print(dataFrame[dataFrame["Email Type"] == "Safe Email"]["Email Text"].iloc[0][:300])