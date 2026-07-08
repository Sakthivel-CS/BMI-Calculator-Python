weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in centimeters : "))
height_in_meters = height / 100
bmi = weight / (height_in_meters ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
   print("Normal weight")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
    