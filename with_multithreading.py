import threading
import time
from typing import List

# This script demonstrates the use of Python's threading module for concurrent execution

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

    # With Multithreading
    # Create the two threads
    t1 = threading.Thread(target=square_list, args=(list, squared_result))
    t2 = threading.Thread(target=cube_list, args=(list, cubed_result))

    # Start the threads
    t1.start()
    t2.start()

    # Wait for the threads to finish
    t1.join()
    t2.join()

    end_time = time.time()

    print(f"Squared list: {squared_result}")
    print(f"Cubed list: {cubed_result}")

    print(f"Time taken: {end_time - start_time}")



