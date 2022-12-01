"""Stack implementation using Linked List"""

from typing import Optional, Union
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


class Stack:
    """Stack class implementation."""

    def __init__(self, val: Optional[Union[int, str]] = None):
        """Constructor of the stack object
        Args:
            val: input data
        """
        self.data_list = SinglyLinkedList(val)

    def peek(self) -> Optional[Union[int, str]]:
        """Returns the top value of the stack
        Returns:
            returns the top of the list value if exists
        """
        val: Optional[ListNode] = self.data_list.get_head()
        if val:
            return val.get_val()
        return None

    def push(self, val: Union[int, str]):
        """Adds value to the stack.
        Args:
            val: data value that needs to added to the stack
        """
        self.data_list.add_front(val)

    def pop(self) -> Optional[Union[int, str]]:
        """Remove the top of the stack and return the value
        Returns:
            value of the top of the stack if exists.
        """
        prev_top = self.data_list.remove_head()
        if prev_top:
            return prev_top.get_val()
        return None
