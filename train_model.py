import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("employee_salary_data.csv")
X = df.drop("Salary", axis=1)
y = df["Salary"]
categorical_cols = ['Gender', 'Education', 'JobRole', 'City', 'CompanyType']
numeric_cols = ['Age', 'Experience', 'WorkHours']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first'), categorical_cols)
], remainder='passthrough')

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, 'salary_prediction_model.pkl')
print("✅ Model trained and saved as salary_prediction_model.pkl")
