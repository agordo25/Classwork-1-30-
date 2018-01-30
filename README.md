# Classwork-1-30-
Coding
while True:
print("This program calculates miles per gallon")
miles_driven=float(input("Enter miles_driven"))
gallons_used=float(input("Enter gallons used"))
milesper_gallon=miles_driven/gallons_used
print("Your miles per gallon is:")
print(milesper_gallon)
while True:
    print("This program calculates the area of a rectangle")
    length=float(input("Enter the length:"))
    width=float(input("Enter the width"))
    areaof_rectangle=length*width
    print("The area of the rectangle is:")
    print(areaof_rectangle)
    user_input=input("would you like to perform a new calculation? Y/N")
    if user_input=="Y" or user_input=="y":
                continue
    else:
                break
