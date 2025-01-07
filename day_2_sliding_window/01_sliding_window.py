import random
import time

def brute_force_solution(arr, k):
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        
        max_sum = max(current_sum, max_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(brute_force_solution(arr, k))

def sliding_window_solution(arr, k):
    n = len(arr)

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

print(sliding_window_solution(arr, k))

new_arr = [random.randint(1, 1000) for _ in range(1000000)]
k = 50

start_time = time.time()
sliding_window_solution(new_arr, k)
sliding_window_duration = time.time() - start_time

start_time = time.time()
brute_force_solution(new_arr, k)
brute_force_duration = time.time() - start_time

print(f"Sliding window solution süresi: {sliding_window_duration:.6f} saniye")
print(f"Brute force solution süresi: {brute_force_duration:.6f} saniye")