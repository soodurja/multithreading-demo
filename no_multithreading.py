import time
from typing import List

# This script demonstrates the sequential execution of two functions in Python without multithreading.
# The square_list() and cube_list() functions are run one after the other.
# Since each function includes a delay (time.sleep), the total time taken is the sum of both,
# making it noticeably slower compared to the multithreaded version.


def square_list(nums: List[int], result: List[int]) -> None:
    for num in nums:
        time.sleep(1)
        print(f"Squaring the number {num}")
        result.append(num ** 2)

def cube_list(nums: List[int], result: List[int]) -> None:
    for num in nums:
        time.sleep(1)
        print(f"Cubing the number {num}")
        result.append(num ** 3)

if __name__ == "__main__":
    list = [1, 2, 3, 4]
    squared_result, cubed_result = [], []

    start_time = time.time()

    # Without Multithreading, we sequentially call the two functions
    square_list(list, squared_result)
    cube_list(list, cubed_result)

    end_time = time.time()

    print(f"Squared list: {squared_result}")
    print(f"Cubed list: {cubed_result}")

    print(f"Time taken: {end_time - start_time}")



