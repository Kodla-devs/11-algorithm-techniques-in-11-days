import random
import time
import tracemalloc

def brute_force_solution(grid, i, j):
    if i == 0 and j == 0:
        return grid[i][j]
    if i < 0 or j < 0:
        return float('inf')
    up = brute_force_solution(grid, i - 1, j)
    left = brute_force_solution(grid, i, j - 1)
    return grid[i][j] + min(up, left)

def dynamic_programming_solution(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m -1][n -1]

def create_random_grid(m, n):
    return [[random.randint(1, 9) for _ in range(n)] for _ in range(m)]

def performance_test(grid):
    tracemalloc.start()
    start_time = time.perf_counter()
    result_bf = brute_force_solution(grid, len(grid) - 1, len(grid[0]) - 1)
    end_time = time.perf_counter()
    bf_time = end_time - start_time
    bf_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    tracemalloc.start()
    start_time = time.perf_counter()
    result_dp = dynamic_programming_solution(grid)
    end_time = time.perf_counter()
    dp_time = end_time - start_time
    dp_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(f"grid size {len(grid)} x {len(grid[0])}")
    print(f"brute force result: {result_bf}, time: {bf_time:.6f} second, memory: {bf_memory} byte")
    print(f"dynamic programming result: {result_dp}, time: {dp_time:.6f} second, memory: {dp_memory} byte")
    print("------------------")

m, n = 15, 15
grid = create_random_grid(m, n)

print("grid:")
for row in grid:
    print(row)
print("---------------")

performance_test(grid)