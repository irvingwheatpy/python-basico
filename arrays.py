#find the lowest number in an array.

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0] 

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value: ', minVal)

#how do you print 7 from the following array?

my_array = [7, 12, 9, 4, 11]

print(my_array[0])