import time
import tracemalloc

def brute_force_solution(n):
    if n<= 1:
        return n
    return brute_force_solution(n - 1) + brute_force_solution(n - 2)

def dynamic_programming_solution(n):
    if n <= 1:
        return n
    
    prev1, prev2 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev1, prev2 = prev2, curr
    
    return prev2

n = 45

tracemalloc.start()
start_time = time.perf_counter()
brute_force_result = brute_force_solution(n)
brute_force_time = time.perf_counter() - start_time
brute_force_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_time = time.perf_counter()
optimized_result = dynamic_programming_solution(n)
optimized_time = time.perf_counter() - start_time
optimized_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"brute force result: {brute_force_result}")
print(f"brute force time: {brute_force_time:.6f} second")
print(f"brute force memory: {brute_force_memory[1]} bytes")

print(f"\noptimized dp result: {optimized_result}")
print(f"optimized dp time: {optimized_time:.6f} second")
print(f"optimized memory: {optimized_memory[1]} bytes")