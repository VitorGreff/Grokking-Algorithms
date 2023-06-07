def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])
    
def counter(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + counter(arr[1:])
    
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        x = arr[0]
        if x > find_max(arr[1:]):
            return x
        else:
            # :-1 all the elements but the last one
            # 1: all the elements but the first one
            return find_max(arr[1:])
        
print(sum([2,4,6]))
print(counter([2,4,6]))
print(find_max([2,4,6]))
print(max([2,4,6]))

# 4.5 --> O(n)
# 4.6 --> O(n)
# 4.7 --> O(1)
# 4.8 --> O(n²)