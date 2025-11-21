# Can a function call itself. 
def printNum(num):
    print(num)
    if (num <= 1):
        return -1
    printNum(num-1)

printNum(5)

# Function wait in the memory till they are re-solved. 
# When a function finishes execution, then only it comes out of program and gets deleted from stack.

# fact(n) = n! = n * fact(n-1)
import sys
sys.setrecursionlimit(100)

def factorial(n):
    smallAns = factorial(n-1)
    ans = n*smallAns
    return ans

factorial(5)

# PMI (Principle of Mathematical Induction)
# Recursion principle based on PMI. 

'''
# It is used to prove some fact.
    f(n) = true V n
    where, V -> denotes for all. 

1. Prove F(o) or F(1) is true. 
2. Assume F(k) is true --> Induction Hypothesis. 
3. Using step 2, i.e., F(K) is true.
    Prove that F(k+1) is true. 
''' 

# calculate power2. 
def power2(n):
    if(n==1): # base case. 
        return 2
    smallAnswer = power2(n-1) # Assume (2) -> Induction Hypothesis. 
    ans = 2 * smallAnswer # (3) using (2)
    return ans

print(power2(5))

# Write a Program to find sum of all natural numbers up to a given numbers (n).
# Also, state the recurrence relation and draw the recursion tree. 
def sumNaturalNumberTillN(n):
    # 
    if (n==1):
        return 1 # Base Case (1)

    smallAnswer = sumNaturalNumberTillN(n-1) # Assum that I will get my answer. 
    ans = n + smallAnswer
    return ans

# print(sumNaturalNumberTillN(n))

# Number of Digits.
def number_of_digits(n):
    if (n>=1) and (n<=9):
        return 1
    elif (n==0):
        return 1
    smallNumber = int(n/10)
    smallNumber = number_of_digits(smallNumber)

    ans = 1 + smallNumber

    return ans

print(number_of_digits(9))
print(number_of_digits(123))
print(number_of_digits(546719))

'''
# Find the fibonacci of the numbers. 
# PMI - Extended form. 

1. Proof for base case F(O) F(1)
2. Assume for F(i) equal to true
    where your i can be from 
        0 <= i <= R 

    So, that means we can assume for
        F(R) true 
        F(R-1) true
        - all assume true for less than n. 
'''
functionCallNumber = 1
def fibonacci(n):
    global functionCallNumber
    if (n==0):
        return 1
    if (n==1):
        return 1
    
    last = fibonacci(n-1)
    secondLast = fibonacci(n-2)
    ans = last + secondLast
    return ans

print(fibonacci(12))

# Head Vs Tail Recursion.
# Head Recursion: when we make an recursive call at the begining of our function implementation.
# Tail Recursion: when we make an recursive call at the end of our function implementation.

def tailRecursion(n, accumulator = 1):
    if (n==0):
        return accumulator
    
    accumulator = accumulator * n
    return tailRecursion(n-1, accumulator)

print(tailRecursion(5, 1))

# Write a program for a given number n. 
# 1. Print 1 to N. 
# 2. Print N to 1. 
def print1ToN(n):
    if (n<=0):
        return n
    ans = print1ToN(n-1)
    print(ans)

def printNTo1(n):
    if (n <= 0):
        return n
    ans = printNTo1(n-1)
    return ans
