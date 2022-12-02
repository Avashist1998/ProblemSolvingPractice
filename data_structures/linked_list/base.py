"""Base linked list class definition"""

from abc import ABC, abstractmethod
from typing import Optional, Union


class ListNode(ABC):
    """Abstract class for ListNode data structure."""

    @abstractmethod
    def set_val(self, val: Union[int, str]):
        """Update the value of the node."""

    @abstractmethod
    def set_next(self, node: Optional['ListNode']):
        """Update the value of the next node."""

    @abstractmethod
    def get_val(self) -> Union[int, str]:
        """Returns the value of the node"""

    @abstractmethod
    def get_next(self) -> Optional['ListNode']:
        "Returns the next node"

    @abstractmethod
    def __str__(self) -> str:
        """Returns data as string"""


class LinkedList(ABC):
    """Abasctract class for a LinkedList data structure."""

    @abstractmethod
    def add(self, val: Union[int, str]) -> None:
        """Adds a node the end of the list.
        Args:
            val: int to be added to end of the list
        """

    @abstractmethod
    def remove_head(self) -> Optional[ListNode]:
        """Removes the head node of the list.
        Returns:
            return the previous head of the list
        """

    @abstractmethod
    def __len__(self) -> int:
        """Returns the len of the list.
        Returns:
            number of nodes in the list.
        """

    @abstractmethod
    def __str__(self) -> str:
        """Returns the data as string format"""
