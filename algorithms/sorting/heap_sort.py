"""Heap sort class definition"""

from typing import List
from base import SortingAlgo


class HeapSort(SortingAlgo):
    """HeapSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""
        super().__init__()

    def sort(self, arr: List[int]) -> List[int]:
        """Heap sorting method.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        len_of_arr = len(arr)
        for i in range(len_of_arr // 2 - 1, -1, -1):
            self._heapify(arr, len_of_arr, i)

        for i in range(len_of_arr - 1, 0, -1):
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            self._heapify(arr, i, 0)
        return arr

    def _heapify(self, arr: List[int], length: int, index: int):
        """Heapify an array of numbers."""
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest = index
        if (length > left_index and arr[left_index] > arr[largest]):
            largest = left_index
        if (length > right_index and arr[right_index] > arr[largest]):
            largest = right_index
        if index != largest:
            temp = arr[index]
            arr[index] = arr[largest]
            arr[largest] = temp
            self._heapify(arr, length, largest)


if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6, 7]
    print("The Original Array")
    print(nums)
    sorter = HeapSort()
    nums = sorter.sort(nums)
    print("The Sorted Array")
    print(nums)
