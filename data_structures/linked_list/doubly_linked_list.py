"""Doubly linked list"""

from typing import List, Optional, Union
from data_structures.linked_list.base import ListNode, LinkedList


class DoublyListNode(ListNode):
    """Doubly Linked List Node"""

    def __init__(self, val: Union[int, str]) -> None:
        """Creates a DoublyListNode."""
        self._val = val
        self._next: Optional[ListNode] = None
        self._prev: Optional[ListNode] = None

    def get_val(self) -> Union[int, str]:
        """Returns the value of the node.
        Returns:
            value of the node
        """
        return self._val

    def set_val(self, val: Union[int, str]) -> None:
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

    def set_next(self, node: Optional[ListNode]) -> None:
        """Sets the next node.
        Args:
            node: the new next node of the node.
        """
        self._next = node

    def get_prev(self) -> Optional[ListNode]:
        """Returns the prev node.
        Returns:
            Next prev node if exists
        """
        return self._prev

    def set_prev(self, node: Optional[ListNode]) -> None:
        """Sets the prev node.
        Args:
            node: the new prev node of the node.
        """
        self._prev = node

    def __str__(self) -> str:
        """Returns the data as a string."""
        return f"node val: {self._val}"


class DoublyLinkedList(LinkedList):
    """Doubly Linked List"""

    def __init__(self,
                 data: Optional[Union[int, List[Union[int, str]]]] = None):
        """Creats a Doubly Linked List"""
        self._size: int = 0
        self._head: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None
        self._walker: Optional[ListNode] = None
        if data:
            if isinstance(data, int):
                self._size = 1
                self._head = DoublyListNode(data)
                self._tail = self._head.get_next()
            else:
                if len(data) > 0:
                    self._size = 1
                    self._head = DoublyListNode(data[0])
                    walker: Optional[ListNode] = self._head
                    for val in data[1:]:
                        next_walker = DoublyListNode(val)
                        if walker:
                            next_walker.set_prev(walker)
                            walker.set_next(next_walker)
                            walker = walker.get_next()
                        self._size += 1
                    self._tail = walker

    def add(self, val: Union[int, str]) -> None:
        """Adds element to the end of the List.
        Args:
            node: val added to the back of the list
        """
        node = DoublyListNode(val)
        if self._size == 0:
            self._head = node
            self._tail = self._head.get_next()
        elif self._size == 1 and self._head:
            self._head.set_next(node)
            node.set_prev(self._head)
            self._tail = node
        elif self._tail:
            self._tail.set_next(node)
            node.set_prev(self._tail)
            self._tail = node
        self._size += 1

    def remove_head(self) -> Optional[ListNode]:
        """Removes the head node of the List.
        Returns:
            return the previous head of the list
        """
        prev_head = self._head
        if self._size > 1 and self._head:
            self._head = self._head.get_next()
            assert isinstance(self._head, DoublyListNode)
            self._head.set_prev(None)
            self._size -= 1
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        return prev_head

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

    def get_tail(self) -> Optional[ListNode]:
        """Returns the tail of the list."""
        return self._tail
