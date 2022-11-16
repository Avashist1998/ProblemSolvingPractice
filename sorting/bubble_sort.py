"""Bubble sort class definition"""

from typing import List
from sorting.base import SortingAlgo


class BubbleSort(SortingAlgo):
    """BubbleSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def sort(self, arr: List[int]) -> List[int]:
        """Bubble sorting method.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        sorted_index = len(arr) - 1
        while sorted_index != 0:
            for i in range(0, sorted_index):
                if arr[i] > arr[i - 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

            sorted_index += 1
        return arr
