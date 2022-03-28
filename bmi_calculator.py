"""
BMI = weight/height**2
Underweight : BMI <=18.5
Normal: BMI >= 18.5 and BMI < 25
Overweight: BMI >= 25 and BMI < 30
Obesity: BMI >= 30
- Input: a person's weight & height
- Output : a string, BMI category
"""



while True: 
    print("Please enter your weight (kg):")
    weight = int(input()) #weight in kg
    print("Please enter your height (m):")
    height = float(input()) # height in meter
    bmi = weight//height**2
    print("Your BMI index is: " + str(bmi))
    break

if(bmi <= 18.5):
    print("Underweight")
if(bmi >= 18.5 and bmi < 25):
    print("Normal")
if(bmi >= 25 and bmi < 30):
    print("Overweight")
if(bmi >= 30):
    print("Obesity")