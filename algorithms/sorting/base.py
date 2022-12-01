"""Base sorting class definition"""

from abc import ABC, abstractmethod
from typing import List


class SortingAlgo(ABC):
    """Abasctract class for a sorting algorithm"""

    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        """Sort the input array from least to greatest.
        Args:
            arr: List containing integers.
        Returns:
            sorted array of integers.
        """
