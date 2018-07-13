def CalcMax(mylist):
    maxm = mylist[0]
    for i in mylist:
        if i > maxm:
            maxm = i
    return maxm

x = list(input("Enter the list elements")) #entering list elements from user.
y = CalcMax(x)
print(y)
