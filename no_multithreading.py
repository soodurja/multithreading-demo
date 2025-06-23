import time
from typing import List

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

    # Without Multithreading
    square_list(list, squared_result)
    cube_list(list, cubed_result)

    end_time = time.time()

    print(f"Squared list: {squared_result}")
    print(f"Cubed list: {cubed_result}")

    print(f"Time taken: {end_time - start_time}")



