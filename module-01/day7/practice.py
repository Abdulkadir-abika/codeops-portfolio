#1. Name the Big-O. 
from collections import deque
import bisect
import time
my_list = list(range(1000))
my_dict = {i: i for i in range(1000)}
target = 900
x = my_list[500]
for x in my_list:
    pass
for a in my_list[:10]:
    for b in my_list[:10]:
        pass

value = my_dict[500]
index = bisect.bisect_left(my_list, target)
print("Binary search index:", index)

#2. List vs. dict lookup.
accounts_list = [f"ACC{i}" for i in range(100_000)]
accounts_dict = {f"ACC{i}": i for i in range(100_000)}
target = "ACC99999"
start = time.time()
found = target in accounts_list
print("List lookup time:", time.time() - start)
start = time.time()
found = target in accounts_dict
print("Dict lookup time:", time.time() - start)


#3. Build a stack.
class Stack:
    def init(self):
        self.items = []
    def push(self, item):
        self.items.append(item) 
    def pop(self):
        return self.items.pop()  
    def peek(self):
        return self.items[-1] if self.items else None
names = ["abdu", "riham", "Aaman"]
stack = Stack()
for name in names:
    stack.push(name)
reversed_names = []
while stack.items:
    reversed_names.append(stack.pop())
print("Reversed names:", reversed_names)

# 4.Build a queue. 
queue = deque()
for customer in ["A", "B", "C", "D", "E"]:
    queue.append(customer)
while queue:
    served = queue.popleft()  
    print("Serving:", served)


# 5.Singly linked list. 
class Node:
    def init(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def init(self):
        self.head = None
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    def print_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next  
ll = LinkedList()
for name in ["abdu", "riham", "Aaman"]:
    ll.push_front(name)

print("Linked list contents:")
ll.print_all()