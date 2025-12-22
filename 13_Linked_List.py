'''
# Docstring for 13_Linked_List

# Data Structure --> Data + structure. 

# In-Built Data Structure Python. 
1. List
2. Tuple
3. Dictionary
4. Sets etc

1. LinkedList.
- Add elements as per our requirements -- Basic idea of Linked List. 
- Randomly allocated space in memory. 

Node --> [Data, Address_of_Next_Element]

# Note:- We cannot use .data or .next on my None. 

'''
# Taking input of LinkedList. 

# Return a head to a newly created Linked List.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head

    while(temp != None):
        print(temp.data, end = " -> ")
        temp = temp.next

    print()
    return 

def take_input_better():
    value = int(input("Enter the value of node:- "))
    head = None
    tail = None

    while(value != -1):
        newNode = Node(value)

        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
        value = int(input("Enter the value of node:- "))
    
    return head

newhead = take_input_better()
print_LL(newhead)

# Taking an input of Linked List - Optimized way. 

# Calculating the length of the Linked List. 
# [1 | address_of_2] --> [2 | address_of_3] --> [3 | address_of_3] --> [4 | address_of_4] --> [5 | x address_of_5]

def calculate_length_of_LL(head):
    temp = head
    answer = 0

    while(temp != 0):
        temp = temp.next
        answer = answer + 1

    return answer

def LengthOfLinkedListRecursion(head):

    # 1. Base case. 
    if(head == None):
        return 0
    
    # 2. Recursive Call. 
    recursionAns = LengthOfLinkedListRecursion(head.next)

    # 3. Our Call. 
    return recursionAns + 1

# Operations in LinkedList. 
# 1. Insert
    # - Insert at head. 
    # - Insert at tail. 
    # - Insert in between. 

# 2. Delete
    # - Delete head. 
    # - Delete tail. 
    # - Delete by index. 
    # - Delete by value. 

# 3. Search
    # - Search by index. 
    # - Search by value. 

# 4. Traversal. 
    # - 

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def insert_At_Head_LL(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    # In this condition, head is changed so we have to return the head. 
    return head

head = insert_At_Head_LL(head, 100)

def insert_at_tail_ll(head, data):
    
    temp = head

    newNode = Node(data)

    # If LinkedList is empty then just return the newNode only or newNode becomes the head. 
    if(head == None):
        return newNode
    
    if(temp.next == None):
        temp.next = newNode
        newNode.next = None










