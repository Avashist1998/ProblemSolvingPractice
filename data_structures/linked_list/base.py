"""Base linked list class definition"""

from abc import ABC, abstractmethod


class ListNode(ABC):
    """Abstract class for ListNode data structure."""

    @abstractmethod
    def set_val(self, val: int):
        """Update the value of the node."""

    @abstractmethod
    def set_next(self, node: 'ListNode'):
        """Update the value of the next node."""

    @abstractmethod
    def get_val(self):
        """Returns the value of the node"""

    @abstractmethod
    def get_next(self):
        "Returns the next node"

    @abstractmethod
    def __str__(self) -> str:
        """Returns data as string"""


class LinkedList(ABC):
    """Abasctract class for a LinkedList data structure."""

    @abstractmethod
    def add(self, node: ListNode) -> None:
        """Adds a node the end of the list.
        Args:
            node: node to be added to the list
        """

    @abstractmethod
    def remove_head(self) -> None:
        """Removes the head node of the list."""

    @abstractmethod
    def __len__(self) -> int:
        """Returns the len of the list.
        Returns:
            number of nodes in the list.
        """

    @abstractmethod
    def __str__(self) -> str:
        """Returns the data as string format"""
