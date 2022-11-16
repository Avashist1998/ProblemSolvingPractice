"""Insert sort class definition"""

from typing import List
from base import SortingAlgo


class InsertSort(SortingAlgo):
    """InsertSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def sort(self, arr: List[int]) -> List[int]:
        """Insert sorting method.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        for i in range(1, len(arr)):
            current_val = arr[i]
            j = i - 1

            while (j >= 0 and current_val < arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current_val
        return arr
