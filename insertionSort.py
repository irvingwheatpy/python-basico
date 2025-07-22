#The insertion sort algorithm uses one part of the array to hold the sorted values,
#and another part of the array to hold values that are not sorted yet.

#The algorithm takes one value at a time from the unsorted part of the array and puts it
#into the right place in the sorted part of the array, until the array is sorted.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print('Sorted array: ', my_array)

#or, only shift the values necessary

cool_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(cool_array)

for i in range(1,n):
    insert_index = i
    current_value = cool_array[i]
    for j in range(i-1, -1, -1):
        if cool_array[j] > current_value:
            cool_array[j+1] = cool_array[j]
            insert_index = j
        else:
            break
    cool_array[insert_index] = current_value

print('Sorted array: ', cool_array)