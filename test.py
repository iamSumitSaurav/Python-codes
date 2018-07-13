"If this gets printed, you have learnt something new, so cheers"

def CalcMax(mylist):
    "This will return you the maximum"
    maxm = mylist[0]
    for i in mylist:
        if i > maxm:
            maxm = i
    mylist.append(55)
    mylist.append(23)
    print(mylist)
    return maxm

def CalcMin(mylist):
    "This will return you the minimum"
    minm = mylist[0]
    for i in mylist:
        if i < minm:
            minm = i
    return minm

x = [1, 2, 3, 4, 5, 6]
y = CalcMax(x)
z = CalcMin(x)


