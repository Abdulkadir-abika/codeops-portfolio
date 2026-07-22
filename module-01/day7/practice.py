from collections import deque
import bisect
import time

# 1. Name the Big-O
my_list = list(range(1000))
my_dict = {i: i for i in range(1000)}
target = 900

# List Indexing -> O(1) because Accessing an element by index in a list is constant time 
x = my_list[500]
# Single Loop -> O(n) Iterating through a list scales linearly with the size of the list (n items).
for x in my_list:
    pass

#  O(n^2)  because nested loops over n items are O(n^2).
for a in my_list[:10]:
    for b in my_list[:10]:
        pass

#  Dict Lookup -> O(1)
value = my_dict[500]

#  Binary Search -> O(log n) b/c Binary search divides the search space in half with every step.
index = bisect.bisect_left(my_list, target)
print("Binary search index:", index)

# 2. List vs. dict lookup

accounts_list = [f"ACC{i}" for i in range(100_000)]
accounts_dict = {f"ACC{i}": i for i in range(100_000)}
target_acc = "ACC99999"

start = time.time()
found_in_list = target_acc in accounts_list
list_time = time.time() - start
print("List lookup time:", list_time)

start = time.time()
found_in_dict = target_acc in accounts_dict
dict_time = time.time() - start
print("Dict lookup time:", dict_time)

# 3. Build a stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

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

# 4. Build a queue
queue = deque()

for customer in ["A", "B", "C", "D", "E"]:
    queue.append(customer)

while queue:
    served = queue.popleft()
    print("Serving:", served)

# 5. Singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
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