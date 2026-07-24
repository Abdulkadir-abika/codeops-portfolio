#1. Build a BST. 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
balances = [7, 3, 9, 1, 5, 8, 10]
root = None
for balance in balances:
    root = insert(root, balance)
print("BST In-order:")
inorder(root)
#2.Tree depth
def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1
print("Tree height:")
print(height(root))

#3. Graph BFS 
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return visited
graph =  {"1001": ["1002", "1003"],
    "1002": ["1004"],
    "1003": ["1005"],
    "1004": [],
    "1005": []}
print("Graph BFS:", bfs(graph, '1001'))

#4. Graph DFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

print("DFS:")
print(dfs(graph, "1001"))
#5. Priority queue
import heapq
tasks = [(3, 'write report'), (1, 'email client'),(4, 'team meeting'), (2, 'code review'), (5, 'backup data')]
heapq.heapify(tasks)
print("Priority Queue Output:")
while tasks:
    print(heapq.heappop(tasks))
