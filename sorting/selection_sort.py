"""Slection sort class definition"""

from typing import List
from sorting.base import SortingAlgo


class SlectionSort(SortingAlgo):
    """SlectionSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def sort(self, arr: List[int]) -> List[int]:
        """Slection sorting method.
        Time Complexity: O(nlog(n))
        Space Complexity: O(log(n))
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        for i in range(len(arr) - 1, -1, -1):
            current_max = arr[0]

            for j in range(0, i + 1):
                if current_max < arr[j]:
                    current_max = arr[j]

            arr[i] = current_max
        return arr
