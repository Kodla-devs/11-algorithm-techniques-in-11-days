from itertools import combinations
import time
import tracemalloc

def brute_force_solution(activities):
    n = len(activities)
    max_activities = []

    for r in range(1, n + 1):
        for subset in combinations(activities, r):
            if is_valid_subset(subset):
                if len(subset) > len(max_activities):
                    max_activities = subset
    return max_activities

def is_valid_subset(subset):
    subset = sorted(subset, key=lambda x: x[0])
    for i in range(len(subset) - 1):
        if subset[i][1] > subset[i + 1][0]:
            return False
    return True

def greedy_solution(activities):
    activities.sort(key=lambda x: x[1])
    selected_acitivities = []
    last_end_time = 0

    for activity in activities:
        if activity[0] >= last_end_time:
            selected_acitivities.append(activity)
            last_end_time = activity[1]
    
    return selected_acitivities

def get_fixed_acitivities():
    return [
        (1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9),
        (2, 3), (6, 8), (7, 10), (9, 11), (11, 13), (12, 14),
        (13, 15), (14, 16), (15, 17), (16, 18), (17, 19), (18, 20),
        (10, 13), (20, 22), (21, 23), (22, 24), (23, 25), (24, 26),
    ]

def performance_and_memory_test():
    activities = get_fixed_acitivities()
    print(f"fixed acitivities: {activities}")

    tracemalloc.start()
    start_time = time.perf_counter()
    brute_force_solution(activities)
    end_time = time.perf_counter()
    brute_force_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\n -- brute force -- ")
    print(f"time: {end_time - start_time:.6f} seconds")
    print(f"memory: {brute_force_memory[1]} bytes")
    
    tracemalloc.start()
    start_time = time.perf_counter()
    greedy_solution(activities)
    end_time = time.perf_counter()
    greedy_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\n -- greedy -- ")
    print(f"time: {end_time - start_time:.6f} seconds")
    print(f"memory: {greedy_memory[1]} bytes")

performance_and_memory_test()