BMI CALCULATOR APP
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter height in cm: "))

w = float(weight)
h = float(height) * float(height)

BMI = int(w / h)
print(BMI)

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

w = float(weight)
h = float(height) * float(height)
BMI = round(w / h)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI > 30 and BMI > 35:
    print(f"Your BMI is {BMI}, you are obese ")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")

