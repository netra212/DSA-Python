# Recursion with Arrays/List. 

# Write a Program to check if array is sorted. 
arr = [1,2,3,4,5,6,7]

def check_sorted(arr):
    size = len(arr)

    # 1. Base case. 
    if(size == 1 or size == 1):
        return True
    
    # 2. Recursion call. or Induction hypothesis. 
    ans = check_sorted(arr[1:])

    if(arr[0] < arr[1]):
        return ans
    else:
        return False

def check_sorted2(arr):
    size = len(arr)

    # 1. Base case. 
    if(size == 1 or size == 1):
        return True

    if(arr[0] >= arr[1]):
        return False
    return check_sorted[arr[1:]]

check_sorted(arr)

# Sum of am array using Recursion.
def sum_array(arr):
    if(len(arr) == 1):
        return arr[0]
    
    sum_left_over_array = sum_array(arr[1:])
    ans = sum_left_over_array + arr[0]
    return ans

def sumArray_Tail(arr, accumulator=0):
    if(len(arr) == 0):
        return accumulator
    accumulator += arr[0]

    return sumArray_Tail(arr[1:], accumulator)

sum_array(arr)

# Given an array and an element, find
# a. first index of element. 
# b. last index of element. 
# [3,2,5,2,8,2,1]
# [0,1,2,3,4,5,6]
# ans:
# first_index: 1
# last_index: 5

arr = [3,2,8,5,2,8,2,1]

def firstIndexOfAnElement(arr, num):
    # 1. Base Case. 
    if(len(arr) == 1):
        return -1
     
    x = len(arr)

    # 2.
    if (arr[x] == num):
        return x
    
    ansFromRecursion =  firstIndexOfAnElement(arr[1:], num)

    if (ansFromRecursion == -1):
        return ansFromRecursion
    else:
        return ansFromRecursion + 1

firstIndexOfAnElement(arr, 8)

def lastIndexOfAnElement(arr, num):
    # 1. Base Case. 
    if(len(arr) == 1):
        return -1

'''
# Write a Program to find all index of a given element. 
# Result have to be as below:-
    # a. Print the indexes. 
    # b. Update the answer in list provided. 
    # c. Update indices in the global list. 
    # d. Return answer as a new list. 
'''

l1 = [3,2,8,5,2,8,2,1]
x = 2

def printAllIndicesOfAnElementHelper(l1, x,index):
    if (len(l1) == index):
        return
    
    if(l1[index] == x):
        print(index)

    return printAllIndicesOfAnElementHelper(l1[:],x, index+1)

def printAllIndicesOfAnElement(l1, x):
    # Helper function
    printAllIndicesOfAnElementHelper(l1, x, 0)

printAllIndicesOfAnElement(l1, x)

'''
def find_indices(arr, element):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here
'''

# 
def UpdateAllIndicesOfAnElementInProvidedList(l1, x, index, ansList):
    if (len(l1) == index):
        return

    if(l1[index] == x):
        ansList.append(index)
    
    UpdateAllIndicesOfAnElementInProvidedList(l1, x, index+1, ansList)

ansList = []
UpdateAllIndicesOfAnElementInProvidedList([3,2,5,2,8,2,1],2,0,ansList)


# Update Indices in Global List. 

