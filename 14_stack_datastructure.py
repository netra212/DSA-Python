'''
# Docstring for 14_stack_datastructure

# Stack Data Structures:
    - Linear Data Structure. 
    - LIFO -> Last In First Out. 
    - FILO -> First In Last Out. 
    - Abstract Data Type: Abstract data type is a type for objects whose behaviour is defined by set of operation. 
    - Internally we will be still using the Array, List.

# Industry example of stack. 
    -> Undo, and Redo Operation. 
    -> Call stack in Programming.
    -> Matching html tags.

# stack Mainly used to optimized the problems.

# Operations in Stack. 
    1. Top/peek --> see the top element. 
    2. Pop --> removing the top element. 
    3. Push --> insert an element on top. 
    4. size --> returns no. of elements in our stack. 
    5. Empty --> if our stack is empty or not.
'''

# stack implementation: Using In-Built Python List.

class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"Pushed  {data} into stacked.")
        # print(f"Length of stack is: {len.stack()}")

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        '''
        if(len(self.stack) == 0):
            return True
        else:
            return False
        '''
        return len(self.stack) == 0
    
    def top(self):
        if(self.is_empty()):
            print("stack is empty, not top element")
            return None
        
        # return self.stack[len(self.stack[-1])]

        return self.stack[-1]

    def pop(self): # Gettiing the top element and removing it as well from our stack. 
        if(self.is_empty()):
            print("stack is empty, not top element")
            return None
        
        # return self.stack[len(self.stack[-1])]

        return self.stack.pop()
    
myStack = StackUsingList()

print(myStack.is_empty())
print(myStack.push(1))
print(myStack.push(4))
print(myStack.push(5))
print(myStack.push(6))
print(myStack.push(7))
print(myStack.push(2))
print(myStack.is_empty())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())
print(myStack.top())











