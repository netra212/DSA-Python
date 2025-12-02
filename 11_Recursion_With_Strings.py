# studying Recursion with strings. 
# Recursion is when a problem depends on similar smaller problem.

# Q1. Remove character. 

def remove_characters(s1, ch):

    # 1. Base case: len(s) == 0
    if (len(s1) == 0 or s1 == ''):
        return s1

    # 2. Recursive call: remove char. s[1:]
    smallAnswer = remove_characters(s1[1:], ch)

    if (s1[0] == ch):
        return smallAnswer
    else:
        return s1[0] + smallAnswer

s1 = "good morning zzz"

remove_characters(s1, "z")

# 2. Check Palindrome.
# Palindrom means either from starting and ending, word must be same.
s1 = 'nitin4'
size = len(s1)

print(s1[1: size-1]) # return 2nd: 2nd last

def palindrome_helper(s1, start, end):
    if (start >= end):
        return True
    
    if (s1[start] != s1[end]):
        return False

    return palindrome_helper(s1, start + 1, end - 1)

def check_palindrom(s1):
    return palindrome_helper(s1, 0, len(s1)-1)

'''
# strings: 'abc'

# substring: ordering should be maintain and it should be continous. for a string like abc. `ab`,`bc` are subsequences because it maintain an order but 'ca' cannot be subsequences bcz of not maintaining order. Number of substring: n(n+1)/2.

# subsequences: order should be maintain and they can be non-continous as well which mean for example, abc as a string. ab, bc, ac, but still `ca` cannot be subsequences bcz of not in good order. Number of subsequences: 2^n.

# subsequences of a given strings. 
# abc --> a -> ab, b -> bc, c -> ac, abc, and emptySet. -> Phi

'''

# Q3. strings, substring and subsequences. 
# answers: [a, b, c, ab, bc, ac, abc, empty_set]

def return_subsequences(s1):
    if (s1 == ''): # base case. 
        ans = ['']
        return ans
    
    smallAns = return_subsequences(s1[1:])

    myChar = s1[0]
    ans = []

    ans.extend(smallAns)

    for eachPermutation in smallAns:
        ans.append(myChar + eachPermutation)
        
    return ans

s1 = "abc"
l1 = return_subsequences()



