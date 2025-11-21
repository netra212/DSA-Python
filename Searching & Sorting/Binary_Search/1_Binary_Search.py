# Binary Search: Only apply on the sorted List or Arrays. 
# [10, 23, 35, 45, 50, 70, 85]

# STEPS:

# 1st step: Consider the full array or list. 
# start = 0, end = n - 1

# 2nd step: see the middle element. 
# middle = (end - start) / 2

# 3rd step: Compare element at middle with target. 
# 

# 1st iteration: mid = 3, arr[mid] = 45
# 

sorted_list = [10, 23, 35, 45, 50, 70, 85]
target = 500

def binary_search(arr, target):
    size = len(arr) - 1

    start = 0
    end = size - 1

    while(start <= end):
        mid = (start + end) // 2

        if (arr[mid] == target):
            print("found the target element.")
            return mid
        elif (arr[mid] > target):
            end = mid - 1
        elif (arr[mid] < target):
            start = mid + 1

    return -1
result = binary_search(sorted_list, target)
print(result)




