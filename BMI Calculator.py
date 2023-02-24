print("****BMI CalCulator****\n")
weight = int(input("Enter Your Weight: "))
height = float(input("Enter Your Height: "))
f = weight / height**2
if f < 18.5:
    print("Underweight")
elif f >= 18.5 and f < 25:
    print("Normal")
elif f >= 25 and f < 30:
    print("Overweight")
elif f >= 30:
    print("Obesity")
