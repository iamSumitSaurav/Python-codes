num = int(input("Enter a number"))
count = 0
if num < 2:
    print("Not a prime number")
    
else:
    for x in range(2, num):
        if num % x == 0:
            print("Not a prime number as it is divisible by", x)
            break

    else:
        print("You entered a prime number")
