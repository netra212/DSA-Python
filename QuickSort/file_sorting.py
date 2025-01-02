import random


def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Randomly select a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition the array
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Recursively apply quick sort to partitions
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


# Example usage
trade_volumes = [34, 7, 23, 32, 5, 62]
sorted_volumes = quick_sort(trade_volumes)
print("Sorted trade volumes:", sorted_volumes)
