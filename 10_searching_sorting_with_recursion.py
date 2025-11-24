

'''
# Searching Using Recursion.
    1. Linear Search. 
    2. Binary Search.
'''

def LinearSearchUsingRecursion(l1, x, index):
    # Base Case. 
    if (len(l1) == index):
        return False
    
    if(l1[index] == x):
        return True
    
    return LinearSearchUsingRecursion(l1, x, index+1)
    
ans = LinearSearchUsingRecursion([1, 4, 3, 2, 6, 5, 8], 2, 0)

print(ans)

# 
def BinarySearchUsingRecursionHelper(l1, x, s, e):
    if(s>e):
        return False

    m = s + (e-s)//2

    if (l1[m] == x):
        return True
    
    if ( x > l1[m]):
        s = m + 1
        return BinarySearchUsingRecursionHelper(l1, x, s, e)
    
    s = m - 1
    return BinarySearchUsingRecursionHelper(l1, x, s, e)

def BinarySearchUsingRecursion(l1, x):
    return BinarySearchUsingRecursionHelper(l1, x, 0, len(l1)-1)

# 
'''
Sorting Using Recursion. 
# Merge Sort. 
'''

l1 = [5, 1, 6, 8, 3, 9, 2, 10]

def Merge(l1, s, m, e):
    i = s 
    j = m+1
    ans = []
    
    # Left part condition and right part condition.
    while(i <= m and j <= e):
        # adding left part. 
        if (l1[i] < l1[j]):
            ans.append(l1[i])
            i+=1
        # adding right part.    
        elif (l1[i] > l1[j]):
            ans.append(l1[j])
            j+=1
        elif(l1[i] == l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i+=1
            j+=1

    while(i<=m):
        ans.append(l1[i])
        i+=1
    
    while(j <= e):
        ans.append(l1[j])
        j+=1

    # Now, Just copying to the original List l1. 
    startOfMyAns = 0
    startOfMyList = s  

    # running loop to end of original list. 
    while(startOfMyList <= e):
        l1[startOfMyList] = ans[startOfMyAns]
        startOfMyAns+=1

def MergeSortHelper(l1,s,e):
    if(s >= e):
        return
    
    m = s + (e-s)//2
    
    MergeSortHelper(l1, s, m) # calling left half. 
    MergeSortHelper(l1, m+1, e) # calling right half. 

    Merge(l1, s, m, e)

    return

def MergSort(l1):
    return MergeSortHelper(l1, 0, len(l1)-1)

MergSort(l1)
print(l1)

'''
# Quick Sort Implementation.
# In Quick sort, unlike merge sort, we first do our work and then let recursion handle the rest.
'''

def partitionFunction(l1, s, e):
    # Taking pivot as last element. 
    pivot = l1[e]

    i = s
    rightPosition = s

    while(i <= e-1):
        if(l1[i] < pivot):
            rightPosition += 1
        i+=1
    l1[rightPosition], l1[e] = l1[e], l1[rightPosition]

    pivotIndex = rightPosition
    
    start = s 
    end = e

    while(start < pivotIndex and end > pivotIndex):
        if(l1[start] < pivot):
            start+=1
        elif(l1[end] >= pivot):
            end-=1
        else:
            l1[start], l1[end] = l1[end], l1[start]
            start+=1
            end-=1

    return pivotIndex

def QuickSort(l1, s, e):
    if (s>=e):
        return

    pivotIndex = partitionFunction(l1, s, e)

    QuickSort(l1, s, pivotIndex-1)
    QuickSort(l1, pivotIndex + 1, e)


l1 = [5, 1, 6, 8, 3, 9, 2, 10]

QuickSort(l1, 0, len(l1)-1)
print(l1)

