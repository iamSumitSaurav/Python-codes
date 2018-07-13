def maximum(mylist):
    return max(mylist)


mylist = []
i = 1
length = int(input('Give the size of the list'))
for x in range(0, length):
    x = input("Enter element {}.".format(i))
    mylist.append(x)
    i = i+1

print(mylist)
y = maximum(mylist)
print("The maximum element is {}: ".format(y))
