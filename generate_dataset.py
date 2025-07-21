import pandas as pd
import numpy as np
import random

genders = ['Male', 'Female', 'Other']
education_levels = ['Bachelors', 'Masters', 'PhD']
job_roles = ['Developer', 'Manager', 'Analyst', 'HR', 'Designer', 'Tester', 'Tech Lead',
             'Data Scientist', 'System Admin', 'Consultant']
cities = ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad', 'Pune',
          'Kolkata', 'Ahmedabad', 'Jaipur', 'Kochi']
company_types = ['Startup', 'MNC', 'Government', 'Mid-size', 'Consultancy', 'NGO', 'Product-Based']

def generate_salary_data(n=500):
    data = []
    for _ in range(n):
        age = random.randint(21, 60)
        gender = random.choice(genders)
        edu = random.choice(education_levels)
        role = random.choice(job_roles)
        exp = random.randint(0, 40)
        city = random.choice(cities)
        company = random.choice(company_types)
        hours = random.randint(30, 60)
        salary = 20000 + (exp * 1500) + (education_levels.index(edu) * 5000)
        if company == 'MNC': salary += 10000
        elif company == 'Product-Based': salary += 12000
        elif company == 'Startup': salary += 5000
        elif company == 'Consultancy': salary += 8000
        elif company == 'Government': salary += 6000
        if role in ['Manager', 'Tech Lead']: salary += 15000
        elif role == 'Data Scientist': salary += 20000
        elif role == 'Consultant': salary += 12000
        if city in ['Bangalore', 'Mumbai', 'Delhi']: salary += 5000
        salary += random.randint(-7000, 7000)
        data.append([age, gender, edu, role, exp, city, company, hours, int(salary)])
    df = pd.DataFrame(data, columns=['Age', 'Gender', 'Education', 'JobRole', 'Experience',
                                     'City', 'CompanyType', 'WorkHours', 'Salary'])
    return df

df = generate_salary_data()
df.to_csv("employee_salary_data.csv", index=False)
print("✅ Dataset created and saved as employee_salary_data.csv")
