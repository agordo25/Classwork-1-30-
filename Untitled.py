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
