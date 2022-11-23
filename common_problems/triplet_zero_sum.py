"""Sum of 3 problem solution"""
from time import time
from typing import List


def naive_approch(arr: List[int], size: int):
    """Naive approch solution.
    Args:
        arr: list of number
        size: length of the array
    Return:
        list containing all possible solutions.
    """
    output = []
    for i in range(size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == 0:
                    output.append([arr[i], arr[j], arr[k]])
    return output


def hash_approch(arr: List[int], size: int):
    """Hashmap approch solution.
    Args:
        arr: list of number
        size: length of the array
    Return:
        list containing all possible solutions.
    """
    output = []
    for i in range(size - 1):
        set_of_arr = set()
        for j in range(i + 1, size):
            target = -1 * (arr[i] + arr[j])
            if target in set_of_arr:
                output.append([target, arr[i], arr[j]])
            else:
                set_of_arr.add(arr[j])
    return output


def sort_approch(arr: List[int], size: int):
    """Sorting approch solution.
    Args:
        arr: list of number
        size: length of the array
    Return:
        list containing all possible solutions.
    """
    arr.sort()
    output = []
    for i in range(size - 1):
        left = i + 1
        right = size - 1
        while left < right:
            if arr[left] + arr[right] == -1 * arr[i]:
                output.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif arr[left] + arr[right] < -1 * arr[i]:
                left += 1
            else:
                right -= 1
    return output


nums = [0, -1, 2, -3, 1]
startNaive = time()
print(naive_approch(nums, len(nums)))
print(f"Time of the nieve approch :{time()-startNaive}")

startHash = time()
print(hash_approch(nums, len(nums)))
print(f"Time of the hash approch {time()-startHash}")

startSort = time()
print(sort_approch(nums, len(nums)))
print(f"Time of the sort apporch {time()-startSort}")
