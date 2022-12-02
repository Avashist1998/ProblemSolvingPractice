"""Remove duplicate nodes"""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def remove_duplicates(root: ListNode):
    """Removes duplicate from a singly linked list"""
    val_set = set()
    walker: ListNode = root
    val_set.add(root.get_val())
    while walker.get_next():
        walker_next: Optional[ListNode] = walker.get_next()
        if walker_next and walker_next.get_val() in val_set:
            new_next = walker_next.get_next()
            walker.set_next(new_next)
        else:
            if walker_next:
                val_set.add(walker_next.get_val())
                walker = walker_next


class TestRemoveDuplicate(unittest.TestCase):
    """Test the remove duplicate method."""

    def test_one_value_case(self):
        """Test the one value case."""
        a_list = SinglyLinkedList(1)
        remove_duplicates(a_list.get_head())
        self.assertEqual(str(a_list), "[1]")

    def test_all_duplicate_case(self):
        """Test all duplicated case."""
        a_list = SinglyLinkedList([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])
        remove_duplicates(a_list.get_head())
        self.assertEqual(str(a_list), "[1 -> 2 -> 3]")

    def test_even_duplicate_case(self):
        """Test even number of duplicate cases."""
        values = [1, 2, 4, 2, 6, 8]
        expected_values = ["1", "2", "4", "6", "8"]
        a_list = SinglyLinkedList(values)
        remove_duplicates(a_list.get_head())
        expected = "[" + " -> ".join(expected_values) + "]"
        self.assertEqual(str(a_list), expected)

    def test_odd_duplicate_case(self):
        """Test odd number of duplicate cases."""
        values = [1, 2, 2, 4, 9, 2, 6, 8]
        expected_values = ["1", "2", "4", "9", "6", "8"]
        a_list = SinglyLinkedList(values)
        remove_duplicates(a_list.get_head())
        expected = "[" + " -> ".join(expected_values) + "]"
        self.assertEqual(str(a_list), expected)


if __name__ == "__main__":
    unittest.main()
