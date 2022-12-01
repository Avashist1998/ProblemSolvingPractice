""""Queue impelementation"""

from typing import Optional, Union
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


class Queue:
    """Queue class implementation."""

    def __init__(self, val: Optional[Union[int, str]] = None):
        """Constructor of the Queue object
        Args:
            val: input data
        """
        self.data_list = SinglyLinkedList(val)

    def add_item(self, val: Union[int, str]):
        """Adds value to the queue.
        Args:
            val: data value that needs to added to the stack.
        """
        self.data_list.add(val)

    def remove_item(self) -> Optional[Union[int, str]]:
        """Remove the first value of the queue and return the value.
        Returns:
            value at the front of the queue if exists.
        """
        prev_first = self.data_list.remove_head()
        if prev_first:
            return prev_first.get_val()
        return None

    def peek(self) -> Optional[Union[int, str]]:
        """Returns the first value of the queue
        Returns:
            returns the first of the queue value if exists.
        """
        val: Optional[ListNode] = self.data_list.get_head()
        if val:
            return val.get_val()
        return None

    def is_empty(self) -> bool:
        """Checks if the queue is empty.
        Returns:
            returns True if queue is empty and False otherwise
        """
        if self.data_list.get_head():
            return True
        return True
