"""Singly LinkedList Implementation"""

from typing import List, Optional, Union
from base import LinkedList, ListNode


class SinglyListNode(ListNode):
    """Singly Linked List Node"""

    def __init__(self, val: int) -> None:
        """Creates a SinglyListNode."""
        self._val = val
        self._next: Optional[ListNode] = None

    def get_val(self) -> int:
        """Returns the value of the node.
        Returns:
            value of the node
        """
        return self._val

    def set_val(self, val: int) -> None:
        """Sets the value of the node.
        Args:
            val: the new value of the node.
        """
        self._val = val

    def get_next(self) -> Optional[ListNode]:
        """Returns the next node.
        Returns:
            Next node if exists
        """
        return self._next

    def set_next(self, node: ListNode) -> None:
        """Sets the next node.
        Args:
            node: the new next node of the node.
        """
        self._next = node

    def __str__(self) -> str:
        """Returns the data as a string."""
        return f"node val: {self._val}"


class SinglyLinkedList(LinkedList):
    """Singly Linked List"""

    def __init__(self, data: Optional[Union[int, List[int]]] = None):
        """Creats a Singly Linked List"""
        self._size: int = 0
        self._head: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None
        self._walker: Optional[ListNode] = None
        if data:
            if isinstance(data, int):
                self._size = 1
                self._head = SinglyListNode(data)
                self._tail = self._head.get_next()
            else:
                if len(data) > 0:
                    self._size = 1
                    self._head = SinglyListNode(data[0])
                    walker: Optional[ListNode] = self._head
                    for val in data[1:]:
                        next_walker = SinglyListNode(val)
                        if walker:
                            walker.set_next(next_walker)
                            walker = walker.get_next()
                        self._size += 1
                    self._tail = walker

    def add(self, node: ListNode) -> None:
        """Adds element to the end of the List.
        Args:
            node: noded added to the back of the list
        """
        if self._size == 0:
            self._head = node
            self._tail = self._head.get_next()
        elif self._size == 1 and self._head:
            self._head.set_next(node)
            self._tail = node
        elif self._tail:
            self._tail.set_next(node)
            self._tail = node
        self._size += 1

    def remove_head(self) -> None:
        """Removes the head node of the List."""
        if self._size > 1 and self._head:
            self._head = self._head.get_next()
            self._size -= 1
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
        else:
            pass

    def __len__(self) -> int:
        """Returns the size of the List"""
        return self._size

    def __iter__(self):
        """Intialize the walker"""
        self._walker = self._head
        return self

    def __next__(self):
        """Returns the next node of the List"""
        if self._size and self._walker:
            node = self._walker
            self._walker = self._walker.get_next()
            return node
        raise StopIteration

    def __str__(self) -> str:
        """Returns the data as a string"""
        res = "["
        for node in self:
            res += f"{node.get_val()} -> "
        res = res[:-4] + "]"
        return res

    def get_head(self) -> Optional[ListNode]:
        """Returns the head of the list."""
        return self._head
