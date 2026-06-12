import numpy as np
import matplotlib.pyplot as plt

# Dataset
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
grades = np.array([45, 50, 55, 65, 70, 75, 85, 90])

# Least Squares Method
n = len(hours)

a = (n * np.sum(hours * grades) -
     np.sum(hours) * np.sum(grades)) / (
     n * np.sum(hours**2) -
     (np.sum(hours))**2)

b = (np.sum(grades) - a * np.sum(hours)) / n

print(f"Slope (a) = {a:.2f}")
print(f"Intercept (b) = {b:.2f}")

# Prediction
study_hours = float(input("Enter study hours: "))
predicted_grade = a * study_hours + b

print(f"Predicted grade: {predicted_grade:.2f}")

# Plot
plt.scatter(hours, grades, label="Data")
plt.plot(hours, a * hours + b, label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")
plt.title("Student Grade Prediction")
plt.legend()
plt.show()