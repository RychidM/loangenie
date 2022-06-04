import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('train.csv')

df = df.drop(['Loan_ID'], axis = 1)

df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
df['Married'].fillna(df['Married'].mode()[0],inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)

df['Gender'] = df['Gender'].replace(('Male','Female'),(1, 0))
df['Married'] = df['Married'].replace(('Yes','No'),(1, 0))
df['Education'] = df['Education'].replace(('Graduate','Not Graduate'), (1, 0))
df['Self_Employed'] = df['Self_Employed'].replace(('Yes','No'), (1, 0))
df['Loan_Status'] = df['Loan_Status'].replace(('Y','N'), (1, 0))
df['Property_Area'] = df['Property_Area'].replace(('Urban','Semiurban', 'Rural'),(2, 1, 0))
df['Dependents'] = df['Dependents'].replace(('0', '1', '2', '3+'), (0, 1, 2, 3))

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

df.ApplicantIncome = np.sqrt(df.ApplicantIncome)
df.CoapplicantIncome = np.sqrt(df.CoapplicantIncome)
df.LoanAmount = np.sqrt(df.LoanAmount)

X = df.drop(["Loan_Status"], axis=1)
y = df["Loan_Status"]

X, y = SMOTE().fit_resample(X, y)

X = MinMaxScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

for i in range(2,21):
    DTclassifier = DecisionTreeClassifier(max_leaf_nodes=i)
    DTclassifier.fit(X_train, y_train)

file = open('dtModel.pkl', 'wb')
pickle.dump(DTclassifier, file)


