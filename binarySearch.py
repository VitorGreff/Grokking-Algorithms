def binarySearch(arr, low, high, x):
    # caso base
    arr.sort()
    if low <= high:
        mid = (high + low)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr, mid+1, high, x)
        else:
            return binarySearch(arr, low, mid-1, x)
    else:
        return None



list = [2,3,1,4,5,6]
print(binarySearch(list, 0, len(list) - 1, 6))
