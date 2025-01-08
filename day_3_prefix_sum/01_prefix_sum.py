import random
import time
import tracemalloc

def brute_force_solution(arr, queries):
    result = []
    for l, r in queries:
        total = 0
        for i in range(l - 1, r):
            total += arr[i]
        result.append(total)
    return result

arr = [3, 6, 2, 8, 9, 2]
queries = [(2, 5), (4, 6), (1, 5), (3, 6)]
print("Brute force sonuçları: ", brute_force_solution(arr, queries))

def prefix_sum_solution(arr, queries):
    n = len(arr)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    result = []
    for l, r in queries:
        result.append(prefix_sum[r] - prefix_sum[l - 1])
    return result

print("prefix sum sonucları: ", prefix_sum_solution(arr, queries))


n = 10**5
q = 10**3

arr = [random.randint(1, 1000) for _ in range(n)]
queries = [(random.randint(1, n // 2), random.randint(n // 2, n)) for _ in range(q)]

tracemalloc.start()
start_time = time.time()
prefix_sum_result = prefix_sum_solution(arr, queries)
prefix_sum_duration = time.time() - start_time
prefix_sum_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
brute_force_result = brute_force_solution(arr, queries)
brute_force_duration = time.time() - start_time
brute_force_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Prefix sum süresi: {prefix_sum_duration:.6f} saniye")
print(f"Brute force süresi: {brute_force_duration:.6f} saniye")

print(f"Prefix sum bellek kullanımı: {prefix_sum_memory[1] / 1024:.2f} KB")
print(f"Brute force bellek kullanımı: {brute_force_memory[1] / 1024:.2f} KB")