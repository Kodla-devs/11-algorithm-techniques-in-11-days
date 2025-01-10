from collections import deque
import random
import time
import tracemalloc

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_preorder(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def generate_random_graph(n):
    if n==0:
        return None
    nodes = [Node(random.randint(1, 100)) for _ in range(n)]
    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

NUM_NODES = 8388608
root = generate_random_graph(NUM_NODES)

tracemalloc.start()
start_time = time.time()
dfs_preorder(root)
dfs_time = time.time() - start_time
dfs_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
bfs(root)
bfs_time = time.time() - start_time
bfs_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("dfs time: ", dfs_time)
print("dfs memory: ", dfs_memory)
print("bfs time: ", bfs_time)
print("bfs memory: ", bfs_memory)
