import random

def smallest_element(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest = smallest_element(arr)
        sorted_array.append(arr.pop(smallest))
    return sorted_array

array = [random.randint(1, 100) for _ in range(100)]
print(array)
print(selection_sort(array))




        