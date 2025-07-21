#go through array to find lowest value.
#Move the lowest value to the front of the unsorted part of the array.
#Go through the array again as many times as there are values in the array.

#We need an array with values to sort
#an inner loop that goes through the array, finds the lowest value and moves it to the front of the array.
#This loop must loop through one less value each time it runs.
#An outer loop that controls how many times the inner loop must run. 
#For an array with n values, this outer loop must run n-1 times.

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print('Sorted Array: ', my_array)

#Instead of removing the value, placing it in front of the array and shifting the other valus, you can swap values.

better_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(better_array)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if better_array[j] < better_array[min_index]:
            min_index = j
    better_array[i], better_array[min_index] = better_array[min_index], better_array[i]

print('Sorted array: ', better_array)