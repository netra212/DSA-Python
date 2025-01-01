# Quick sort is an sorting algorithms.
# Quick sort follows the divide and conquer method to sort an elements.


'''
# Algorithms:
arr =  [ 10, 16, 8, 12, 15, 3, 9, 6 ]
------------------------------------------------------
select pivot element.
    Question: How to select the pivot element ?
        a. Randomly.
        b. Median.
        c. 1st element.
        d. Last element.
    Usually, we take last element as 'Pivot' element.
    pivot_element = 6
    Our Jobs is to arrange the elements on the basis of the
    pivot-element.
    If other_element < pivot_element => arrange at left.
    If other_element > pivot_element => arrange at right.

------------------------------------------------------
'''


# Function to find the partition position.
def partition(arr, low, high):
    # Choose the rightmost element as pivot element.
    pivot_element = arr[high]
    # `i` -> is a pointer to keep track of the elements smaller than pivot.
    # Assuming that there are no any element lesser than pivot element.
    i = low - 1  # pointer for greater element.

    # Traversing through all the element and compare each element with pivot.
    for j in range(low, high):
        if arr[j] < pivot_element:
            # If element smaller than pivot is found.
            i = i + 1
            # then swap it with greater element pointed by i.
            # swapping the pivot element with the greater element specified by i.
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # At the end, pivot is swapped with the pointer.
    i = i + 1
    temp = arr[i]
    arr[i] = pivot_element
    arr[high] = temp
    # Return the position from where the parition is performed.
    return i  # return pivot index.


def quick_sort(arr, low, high):
    if low < high:
        pivot_element = partition(arr, low, high)
        # once, we found the correct position of the pivot element, then
        # We have to sort the left element less than pivot and right element
        # greater than pivot.

        # CASE 1: sorting elements less than pivot element.
        quick_sort(arr, low, pivot_element - 1)

        # CASE 2: sorting elements greater than pivot element.
        quick_sort(arr, pivot_element+1, high)


if __name__ == "__main__":
    print("\nQuick-Sort-Implementation\n")
    arr = [10, 16, 8, 12, 15, 3, 9, 6]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    for i in range(n):
        print(arr[i], end=" ")

print("\n")

'''
Time Complexity:
Worst: O(n^2)
Average: O(nlogn)
Important Note: Worst Case occurs when pivot is always the smallest or the
largest element.
'''
