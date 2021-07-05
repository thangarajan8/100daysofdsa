class node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next
            
def createList(arr,n):
    lis = LinkedList()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
from math import ceil, floor
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(arr)
head = createList(arr,n)
values = []
while head:
    values.append(head.data)
    head = head.next
print(values)

x = floor(len(values)/2)
print(values[x])