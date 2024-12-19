def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif bmi >= 30:
        return "Obese"

# Example usage
bmi = float(input("Enter your BMI: "))
print("Your BMI category is:", classify_bmi(bmi))
