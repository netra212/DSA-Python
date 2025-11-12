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




