num = int(input("Enter a number"))
d = 2
print("The prime factors of {} are:".format(num))
while(num > 1):
    if(num % d == 0):
        print(d)
        num = num / d
        continue
    d = d + 1
