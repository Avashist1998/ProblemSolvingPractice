"""Merge sort class definition"""

from typing import List
from base import SortingAlgo


class MergeSort(SortingAlgo):
    """MergeSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def merge_routine(self, arr_a: List[int], arr_b: List[int]) -> List[int]:
        """Merge routine of the sorting algorithm."""
        res = []
        while (len(arr_a) > 0 or len(arr_b) > 0):
            if len(arr_a) == 0:
                res.append(arr_b.pop(0))

            elif len(arr_b) == 0:
                res.append(arr_a.pop(0))

            elif arr_a[0] < arr_b[0]:
                res.append(arr_a.pop(0))
            else:
                res.append(arr_b.pop(0))
        return res

    def sort(self, arr: List[int]) -> List[int]:
        """Merge sorting method.
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        if len(arr) == 1:
            pass
        elif len(arr) == 2:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]

        else:

            mid = len(arr) // 2

            left, right = arr[:mid], arr[mid:]
            left, right = self.sort(left), self.sort(right)
            sorted_arr = self.merge_routine(left, right)

            for i, _ in enumerate(arr):
                arr[i] = sorted_arr[i]
        return arr
