from itertools import combinations
import random
import time
import tracemalloc

def brute_force_solution(nums, target):
    n = len(nums)
    result = []
    operation_count = 0
    for r in range(n + 1):
        for subset in combinations(nums, r):
            operation_count += 1
            if sum(subset) == target:
                result.append(list(subset))
    return result, operation_count

def backtracking_solution(nums, target):
    def backtrack(index, current_sum, path):
        nonlocal operation_count
        operation_count += 1
        if current_sum == target:
            result.append(path)
            return
        if current_sum > target or index >= len(nums):
            return
        backtrack(index + 1, current_sum + nums[index], path + [nums[index]])
        backtrack(index + 1, current_sum, path)

    result = []
    operation_count = 0
    backtrack(0, 0, [])
    return result, operation_count

random.seed(42)
nums = random.sample(range(1, 500), 25)
target = random.randint(200, 800)

def measure_performance(function, nums, target):
    tracemalloc.start()
    start_time = time.perf_counter()
    result, operation_count = function(nums, target)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        "operation_count": operation_count,
        "time": end_time - start_time,
        "memory": peak / 1024
    }

print(f"liste: {nums}")
print(f"hedef: {target}")

brute_forc_perf = measure_performance(brute_force_solution, nums, target)
print(f"\nbrute force")
print(f"toplam islem sayisi: {brute_forc_perf["operation_count"]}")
print(f"zaman: {brute_forc_perf["time"]:.6f} saniye")
print(f"bellek: {brute_forc_perf["memory"]:.6f} kb")

backtracking_perf = measure_performance(backtracking_solution, nums, target)
print(f"\nbacktracking")
print(f"toplam islem sayisi: {backtracking_perf["operation_count"]}")
print(f"zaman: {backtracking_perf["time"]:.6f} saniye")
print(f"bellek: {backtracking_perf["memory"]:.6f} kb")