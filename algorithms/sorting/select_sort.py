"""Select sort class definition"""

from typing import List
from base import SortingAlgo


class SelectSort(SortingAlgo):
    """Select Sort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def sort(self, arr: List[int]) -> List[int]:
        """Select sorting method.
        Time Complexity: O(nlog(n))
        Space Complexity: O(log(n))
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
        for i in range(len(arr) - 1, -1, -1):
            max_index = 0
            current_max = arr[0]
            for j in range(0, i + 1):
                if current_max < arr[j]:
                    current_max = arr[j]
                    max_index = j

            arr[i], arr[max_index] = current_max, arr[i]
        return arr
