"""Detects a loop in a list."""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def detect_loop(head: ListNode) -> bool:
    """Detects the loop in a list.
    Args:
        head: root node of the list.
    Returns:
        Returns true if a loop is detected or false
    """
    slow_runner: Optional[ListNode] = head
    fast_runner: Optional[ListNode] = head

    while (slow_runner and fast_runner):
        slow_runner = slow_runner.get_next()
        fast_runner_next: Optional[ListNode] = fast_runner.get_next()
        fast_runner = fast_runner_next.get_next() if fast_runner_next else None

        if slow_runner == fast_runner:
            return True
    return False


class TestDetectLoop(unittest.TestCase):
    """Test detect loop function."""

    def test_no_loop_case(self):
        """Test the no loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        self.assertFalse(detect_loop(root_node))

    def test_even_loop_case(self):
        """Test even lenght loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node.get_next())
        self.assertTrue(detect_loop(root_node))

    def test_odd_loop_case(self):
        """Test odd lenght loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node.get_next().get_next())
        self.assertTrue(detect_loop(root_node))

    def test_head_loop_case(self):
        """Test head loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node)
        self.assertTrue(detect_loop(root_node))


if __name__ == "__main__":
    unittest.main()
