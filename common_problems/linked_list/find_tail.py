"""Find the of a rotating list."""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def find_tail(node: ListNode) -> Optional[ListNode]:
    """Find the tail of a rotating linked list.
    Args:
        node: head node of a rotating list.
    Returns:
        tail node of the input list.
    """
    slow_runner: Optional[ListNode] = node
    fast_runner: Optional[ListNode] = node

    while fast_runner and fast_runner.get_next():
        if slow_runner:
            slow_runner = slow_runner.get_next()
        fast_runner_next = fast_runner.get_next()
        if fast_runner_next:
            fast_runner = fast_runner_next.get_next()
        if slow_runner == fast_runner:
            break

    if fast_runner is None or fast_runner.get_next() is None:
        return None

    slow_runner = node
    while slow_runner != fast_runner:
        if fast_runner:
            fast_runner = fast_runner.get_next()
        if slow_runner:
            slow_runner = slow_runner.get_next()
    return slow_runner


class TestFindTail(unittest.TestCase):
    """Test detect loop function."""

    def test_no_loop_case(self):
        """Test the no loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        self.assertIsNone(find_tail(root_node))

    def test_even_loop_case(self):
        """Test even lenght loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node.get_next())
        self.assertEqual(find_tail(root_node), root_node.get_next())

    def test_odd_loop_case(self):
        """Test odd lenght loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node.get_next().get_next())
        self.assertTrue(find_tail(root_node), root_node.get_next().get_next())

    def test_head_loop_case(self):
        """Test head loop case."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root_node = SinglyLinkedList(values).get_head()
        walker = root_node
        while walker.get_next():
            walker = walker.get_next()
        walker.set_next(root_node)
        self.assertTrue(find_tail(root_node), root_node)


if __name__ == "__main__":
    unittest.main()
