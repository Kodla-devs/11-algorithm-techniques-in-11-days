import random
import time

def brute_force_solution(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):

            if arr[i] + arr[j] == target:
                return True
    
    return False

arr = [10, 20, 35, 45, 50]
target = 65

result = brute_force_solution(arr, target)
print(result)

def two_pointer_solution(arr, target):
    arr.sort()

    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

result = two_pointer_solution(arr, target)

print(result)

new_arr = [random.randint(1, 1000) for _ in range(10000)]
target = 1500

start_time = time.time()
two_pointer_solution(new_arr, target)
two_pointer_duration = time.time() - start_time

start_time = time.time()
brute_force_solution(new_arr, target)
brute_force_duration = time.time() - start_time

print(f"Two pointer solution süresi: {two_pointer_duration:.6f} saniye")
print(f"Brute force solution süresi: {brute_force_duration:.6f} saniye")