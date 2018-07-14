year = int(input("Enter an year"))

if(year % 100 == 0):
    if(year % 400 == 0):
        print("Yes you have entered a leap year \n")
    else:
        print("This is not a leap year \n")

else:
    if(year % 4 == 0):
        print("Yes you have entered a leap year \n")
    else:
        print("This is not a leap year \n")
        
