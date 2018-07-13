def CalcLargest(list):
   ''' max = list[0]
    for i in range(0, len(list)):
        if(list[i] > max):
            max = list[i]'''
   return max(list)

def CalcSmallest(list):
   ''' min = list[0]
    for i in range(0, len(list)):
        if(list[i] < min):
            min = list[i]'''
   return min(list)

x = list(input("Enter the list elements"))
print("Max value is: ", CalcLargest([x]))
print("Min value is: ", CalcSmallest([x]))
