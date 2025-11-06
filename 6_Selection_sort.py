# Bubble sort. 
# Selection Sort works by repeatedly selecting the smallest element from the unsorted part of the list and placing it at the beginning of the sorted part.

# Think of it like selecting the smallest number from a deck of cards and putting it at the front one by one.

# In each pass, we see the array and select the minimum. 
# We swap that to the right position. 
'''
# Step-by-Step Process:

Let's say we have:

# Find the smallest element → 11
    Swap it with the first element → [11, 25, 12, 22, 64]

Now, Find the next smallest in the remaining list → 12

Swap with second element → [11, 12, 25, 22, 64]

Continue → [11, 12, 22, 25, 64]
'''

def selection_sort(arr):
    size = len(arr)
    
    for i in range(0, size-1):
        for i in range(0, size-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)
print("sorting list with selection sort: ", sorted_list)



