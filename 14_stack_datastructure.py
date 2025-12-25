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
    4. len --> returns no. of elements in our stack. 
    5. Empty --> if our stack is empty or not.
'''

# stack implementation: Using In-Built Python List.

class StackUsingList:
    def __init__(self):
        self.__stack = [] # Very Important to make it private so that functionality is right. 

    def push(self, data):
        self.__stack.append(data)
        print(f"Pushed  {data} into stacked.")
        # print(f"Length of stack is: {len.stack()}")

    def len(self):
        return len(self.__stack)
    
    def is_empty(self):
        '''
        if(len(self.stack) == 0):
            return True
        else:
            return False
        '''
        return len(self.__stack) == 0
    
    def top(self):
        if(self.is_empty()):
            print("stack is empty, not top element")
            return None
        
        # return self.stack[len(self.stack[-1])]

        return self.__stack[-1]

    def pop(self): # Gettiing the top element and removing it as well from our stack. 
        if(self.is_empty()):
            print("stack is empty, not top element")
            return None
        
        # return self.stack[len(self.stack[-1])]

        return self.__stack.pop()
    
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
print(myStack.len())
print(myStack.top())

# Stack Implementation: Using LinkedList. 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class StackUsingLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, data):
        newNode = Node(data)
        self.len += 1 # Very Important to maintain len.
        if(self.head == None):
            self.head = newNode
            return f"Added {data} to the stack"
        
        newNode.next = self.head
        self.head = newNode

        return f"Added {data} to the stack"

    def top(self):
        if(self.head is None or self.len == 0):
            return "Stack is empty, no top element."
        
        return self.head.data
    
    def pop(self):
        if(self.head is None or self.len == 0):
            return "Stack is empty, cannot pop element"
        
        dataAtTop = self.head.data
        self.head = self.head.next
        self.len -= 1

        return dataAtTop

    def len(self):
        return self.len

    def is_empty(self):
        return self.len == 0

myStack = StackUsingLinkedList()








