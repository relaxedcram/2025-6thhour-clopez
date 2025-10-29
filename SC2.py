#Name:Carlos L
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI
Height = int(input("Height in inches "))
weight = int(input("Weight in pounds "))
BMI = weight/(Height**2)*703

if BMI < 18.5:
    print("BMI is underweight")
elif 18.5 <= BMI < 25:
    print("BMI is normal")
elif 25 <= BMI < 30:
    print("BMI is overweight")
else:
    print("BMI is obese")

print(BMI)
#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here: