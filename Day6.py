def calculate_bmi(weight, height):
    return weight / (height ** 2)


print("===== BMI & Health Checker =====")

name = input("Enter Your Name: ")
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = calculate_bmi(weight, height)

print("\n===== RESULT =====")
print(f"Name: {name}")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Status: Underweight")
    print("Suggestion: Increase nutritious food intake and exercise regularly.")

elif bmi < 25:
    print("Status: Normal Weight")
    print("Suggestion: Maintain your healthy lifestyle.")

elif bmi < 30:
    print("Status: Overweight")
    print("Suggestion: Reduce junk food and increase physical activity.")

else:
    print("Status: Obese")
    print("Suggestion: Consult a healthcare professional and follow a healthy diet plan.")
