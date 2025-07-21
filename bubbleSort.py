#Bubble sort runs through an array of 5 values 4 times, swapping each set of numbers each time until the array is sorted.
#Inner loop goes through array and swaps values if the first value is higher than the next value.
#The inner loop must loop through one less value each time it runs.
#Outer loop controls how many times the inner loop must run. For an array with n values, the loop must run n-1 times.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print('Sorted array: ', my_array)

#If the algorithm goes through the array one time without swapping values, the array must be finished sorted.
#In this case, we stop the algorithm.

cool_array = [7, 3, 9, 12, 11]

n = len(cool_array)

for i in range(n-1):
    swapped = False
    for j in range(n - i - 1):
        if cool_array[j] > cool_array[j+1]:
            cool_array[j], cool_array[j+1] = cool_array[j+1], cool_array[j]
            swapped = True
    if not swapped:
        break

print('Sorted Array: ', cool_array)