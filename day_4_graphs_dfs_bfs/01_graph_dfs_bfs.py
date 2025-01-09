from collections import deque
import random
import time
import tracemalloc

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph[node]))
    
    return result

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result

def generate_random_graph(num_nodes, num_edges):
    graph = {i: [] for i in range(1, num_nodes + 1)}
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            graph[u].append(v)
            graph[v].append(u)
            edges.add((u, v))
    return graph

NUM_NODES = 100000
NUM_EDGES = 500000

random_graph = generate_random_graph(NUM_NODES, NUM_EDGES)

tracemalloc.start()
start_time = time.time()
dfs_result = dfs(random_graph, 1)
dfs_time = time.time() - start_time
dfs_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
bfs_result = bfs(random_graph, 1)
bfs_time = time.time() - start_time
bfs_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("Random graph dfs result: visited nodes =", len(dfs_result))
print("dfs time: ", dfs_time)
print("dfs memory: ", dfs_memory)

print("random graph bfs result: visited node =", len(bfs_result))
print("bfs time: ", bfs_time)
print("bfs memory: ", bfs_memory)
    