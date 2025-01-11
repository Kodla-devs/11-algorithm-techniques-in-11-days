import random
import time
import tracemalloc

def brute_force_solution(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        # mid = (low + high) // 2
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_revursive(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_revursive(arr, low, mid - 1, target)
        else:
            return binary_search_revursive(arr, mid + 1, high, target)
    else:
        return -1

def generate_large_list():
    try:
        return sorted(random.sample(range(1, 10**8), 10**6))
    except MemoryError:
        print("memory error: list size exceeds system limits")
        return []
    
algorithms = [ 
    ("brute force solution", lambda lst, target: brute_force_solution(lst, target)),
    ("binary search iterative", lambda lst, target: binary_search_iterative(lst, target)),
    ("binary search recursive", lambda lst, target: binary_search_revursive(lst, 0, len(lst), target))
]

large_list = generate_large_list()
if large_list:
    target = random.choice(large_list)
    for name, func in algorithms:
        tracemalloc.start()
        start_time = time.time()
        start_pref = time.perf_counter()
        func(large_list, target)
        duration_time = time.time() - start_time
        duration_pref = time.perf_counter() - start_pref
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f"algorithm: {name}")
        print(f"time: {duration_time:.6f} s")
        print(f"time pref: {duration_pref:.6f}")
        print(f"memory: {peak}")
        print("------------------")