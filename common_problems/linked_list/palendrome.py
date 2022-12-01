"""Check if a list is a palendrome"""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def is_palendrome_reverse_list(node: ListNode) -> bool:
    """Checks if the list a pandrome using the reverse list method.
    Args:
        input_list: SinglyLinkedList that needs to be checked for a palendrome.
    Returns:
        True is return if the input is a palendrome.
    """

    walker: Optional[ListNode] = node
    reversed_list = SinglyLinkedList()
    while walker:
        reversed_list.add(walker.get_val())
        walker = walker.get_next()

    prev_detached_node = None
    walker = reversed_list.get_head()

    while walker and walker.get_next():
        walker_next = walker.get_next()
        walker.set_next(prev_detached_node)
        prev_detached_node = walker
        walker = walker_next
    if walker:
        walker.set_next(prev_detached_node)

    walker_1: Optional[ListNode] = node
    walker_2: Optional[ListNode] = walker
    while walker_1 and walker_2:
        if walker_1.get_val() != walker_2.get_val():
            return False
        walker_1 = walker_1.get_next()
        walker_2 = walker_2.get_next()
    if walker_1 or walker_2:
        return False
    return True


def is_palendrome_stack(node: ListNode) -> bool:
    """Is linked list a valid palendrome using stack.
    Args:
        node: root node of the linked list.
    Returns:
        True is return if the input is a palendrome.
    """

    stack = []
    slow_runner: Optional[ListNode] = node
    fast_runner: Optional[ListNode] = node
    while slow_runner and fast_runner:
        stack.append(slow_runner.get_val())
        slow_runner = slow_runner.get_next()
        fast_runner_next = fast_runner.get_next()
        if fast_runner_next:
            fast_runner = fast_runner_next.get_next()
        else:
            stack.pop()
            fast_runner = fast_runner.get_next()

    if len(stack) == 0:
        return True
    print(stack)
    while slow_runner:
        if stack:
            if stack.pop() != slow_runner.get_val():
                return False
            slow_runner = slow_runner.get_next()
        else:
            return False
    return True


class TestCheckPalendromeReverseList(unittest.TestCase):
    """Test is_palendrome_stack_reverse_list function"""

    def test_single_case(self):
        """Test single char string case."""
        pal_1 = SinglyLinkedList('a').get_head()
        self.assertTrue(is_palendrome_reverse_list(pal_1))

    def test_valid_even_case(self):
        """Test even number char string valid case."""
        values = ['a', 'n', 'n', 'a']
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertTrue(is_palendrome_reverse_list(pal_1))

    def test_invalid_even_case(self):
        """Test even number char string invalid case."""
        values = ['a', 'n', 'n', 'a', 'a', 'n']
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertFalse(is_palendrome_reverse_list(pal_1))

    def test_valid_odd_case(self):
        """Test odd number char string valid case."""
        values = ["n", "u", "n"]
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertTrue(is_palendrome_reverse_list(pal_1))

    def test_invalid_odd_case(self):
        """Test odd number char string invalid case."""
        values = ["n", "u", "n", "u", "u"]
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertFalse(is_palendrome_reverse_list(pal_1))


class TestCheckIsPalendromeSlack(unittest.TestCase):
    """Test is_palendrome_stack function"""

    def test_single_case(self):
        """Test single char string case."""
        pal_1 = SinglyLinkedList('a').get_head()
        self.assertTrue(is_palendrome_stack(pal_1))

    def test_valid_even_case(self):
        """Test even number char string valid case."""
        values = ['a', 'n', 'n', 'a']
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertTrue(is_palendrome_stack(pal_1))

    def test_invalid_even_case(self):
        """Test even number char string invalid case."""
        values = ['a', 'n', 'n', 'a', 'a', 'n']
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertFalse(is_palendrome_stack(pal_1))

    def test_valid_odd_case(self):
        """Test odd number char string valid case."""
        values = ["n", "u", "n"]
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertTrue(is_palendrome_stack(pal_1))

    def test_invalid_odd_case(self):
        """Test odd number char string invalid case."""
        values = ["n", "u", "n", "u", "u"]
        pal_1 = SinglyLinkedList(values).get_head()
        self.assertFalse(is_palendrome_stack(pal_1))


if __name__ == "__main__":
    unittest.main()
