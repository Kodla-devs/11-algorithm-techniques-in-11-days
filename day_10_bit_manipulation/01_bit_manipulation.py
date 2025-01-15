import time
import tracemalloc

def brute_force_solution(n):
    binary_representation = bin(n)
    return binary_representation.count('1')

def bit_manipulation_solution(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

test_number = 9 * 10**4000

tracemalloc.start()
start_time = time.perf_counter()
brute_force_solution(test_number)
end_time = time.perf_counter()
brute_force_memory = tracemalloc.get_traced_memory()[1]
brute_force_time = end_time - start_time
tracemalloc.stop()

tracemalloc.start()
start_time = time.perf_counter()
bit_manipulation_solution(test_number)
end_time = time.perf_counter()
bit_manipulation_memory = tracemalloc.get_traced_memory()[1]
bit_manipulation_time = end_time - start_time
tracemalloc.stop()

print("\nbrute force time:", brute_force_time)
print("brute force memory:", brute_force_memory)
print("\nbit manipulation time:", bit_manipulation_time)
print("bit manipulation memory:", bit_manipulation_memory, end="\n\n")
