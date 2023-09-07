height = float(input("Enter your height (in meters) : "))
weight = float(input("Enter your weight (in kgs) : "))

bmi = weight / (height) ** 2
print(f"your bodymass index is: {bmi}")

if(bmi <= 18):
    print("Underweight!")

elif(bmi >= 28):
    print("Overweight!")

else:
    print("Normal BMI!")
