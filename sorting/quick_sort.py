"""Quick sort class definition"""

from typing import List
from base import SortingAlgo


class QuickSort(SortingAlgo):
    """QuickSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def sort(self, arr: List[int]) -> List[int]:
        """Quick sorting method.
        Time Complexity: O(nlog(n))
        Space Complexity: O(log(n))
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        if len(arr) > 1:
            pivot = len(arr) - 1
            pivot_val = arr[pivot]
            right, left, equal = [], [], 1

            for i in range(pivot):
                if arr[i] > pivot_val:
                    right.append(arr[i])
                elif arr[i] < pivot_val:
                    left.append(arr[i])
                else:
                    equal += 1

            right, left = self.sort(right), self.sort(left)

            for i, _ in enumerate(arr):
                if len(left) != 0:
                    arr[i] = left.pop(0)
                elif equal != 0:
                    arr[i] = pivot_val
                    equal -= 1
                else:
                    arr[i] = right.pop(0)
        return arr
