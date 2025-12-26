'''
# Docstring for 15_Queue_datastructure.
- Linear Data structure.
- FIFO.
- Abstract Data Type.
- It can be implemented in the backend. 

# Operations in Queue. 
1. enqueue - to add an element into our queue.
2. dequeue - When we remove an element from our queue.
3. size - tell number of elements in our queue.
4. isEmpty - queue empty or not.
5. front - return the element next to come out.
'''
# Queue Implementation: Using In-Built List. 

class QueueUsingList:
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size() == 0 # return True.
    
    def enqueue(self, data):
        self.__queue.append(data)
        return f"We have added {data} to the Queue."
    
    def front(self):
        if(self.size() == 0):
            print("Queue is Empty, cannot show Front")
            return None
        return self.__queue[0]

    def dequeue(self):
        if(self.size() == 0):
            print("Queue is Empty, cannot dequeue")
            return None
        '''
        elementToBeDequeue = self.front()
        self.__queue.pop(0)
        return elementToBeDequeue
        '''
        return self.__queue.pop(0)

Q = QueueUsingList()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
print(Q.size())
print(Q.isEmpty())
print(Q.front())
print(Q.dequeue())
print(Q.dequeue())
print(Q.front())

# Implementing Queue Using LinkedList. 
# 1.enqueue - Possible in O(1). We will have to maintain a tail.
# 2. front(): head.next
# 3. dequeue(): head = head.next
# 4. size(): will have to maintain a length variable for O(1) approach.
# 5. isEmpty(): check is length is zero or head is None. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None
        self.len = 0
    
    def size(self):
        return self.len
    
    def isEmpty(self):
        if(self.size() == 0):
            return True
        
    def enqueue(self, data):
        newNode = Node(data)
        self.len += 1
        if(self.head is None): # My Queue is Empty. 
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        return f"Added {data} to the Queue."

    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty, cannot show front")

        return self.head.data
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty, cannot Dequeue")
            return
        self.len -= 1

        dataToBeReturned = self.head.data
        self.head = self.head.next
        if(self.head == None):
            self.tail = None
        return dataToBeReturned

# Types of Queue. 
# 1. Simple Queue: Single entry and Single exit. 
# LIFO --> Last In First Out. 
# 2. Circular Queue: think like a days in a week in circular form or pie-chart form. 
# 3. Priority Queue:
# 4. Double Ended Queue -> DeQueue.

from collections import deque







