
import pandas as pd

data = {
    "Name": ["Ajay", "priya", "Rahul", "Snehal", "Rohit"],
    "Age": [22, 24, None, 23, 25],
    "Salary": [35000, 25000, 30000, None, 28000]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)
print("Dataset Information:")
df.info()

print("Statistical Analysis:")
print(df.describe())

print("Average Salary:")
print(df["Salary"].mean())

print("Maximum Salary:")
print(df["Salary"].max())

print("Minimum Salary:")
print(df["Salary"].min())

import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Analysis")
plt.show()

print("Highest Salary Employee:")
print(df.loc[df["Salary"].idxmax()])

print("Lowest Salary Employee:")
print(df.loc[df["Salary"].idxmin()])

print("Employees with Salary above 29000:")
print(df[df["Salary"] > 29000])

df.to_csv("cleaned_data.csv", index=False)

print("Cleaned data saved successfully!")

new_df = pd.read_csv("cleaned_data.csv")
print(new_df)

print("Employees older than 23:")
print(df[df["Age"] > 23])

print("Employees with salary between 28000 and 35000:")
print(df[df["Salary"].between(28000, 35000)])

print("===== PROJECT SUMMARY =====")
print("Total Employees:", len(df))
print("Average Age:", round(df["Age"].mean(), 2))
print("Average Salary:", round(df["Salary"].mean(), 2))
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("Missing Values After Cleaning:")
print(df.isnull().sum())

print("Missing values in saved file:")
print(new_df.isnull().sum())

print("Project Completed Successfully!")

