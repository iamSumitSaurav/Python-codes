def sumOfNumbers(a, b, c = 5):
    a = 5
    b = 6
    c = 10
    sum = a+b+c
    return sum
    
x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))
print(sumOfNumbers(x, y, z))
print(x,y,z)
