"""Add two list"""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def add_two_list(list_1: ListNode, list_2: ListNode) -> SinglyLinkedList:
    """Adds two list of numbers.
    Args:
        list_1: 10 base number represented as a list.
        list_2: 10 base number represented as a list.
    Returns:
        Sum of the two number represented as a list.
    """
    total_val = carry = 0
    sum_list = SinglyLinkedList()
    walker_1: Optional[ListNode] = list_1
    walker_2: Optional[ListNode] = list_2
    while (walker_1 or walker_2):
        if carry:
            total_val = carry
            carry = 0
        if walker_1:
            total_val += walker_1.get_val()
            walker_1 = walker_1.get_next()
        if walker_2:
            total_val += walker_2.get_val()
            walker_2 = walker_2.get_next()

        if total_val > 10:
            total_val -= 10
            carry = 1
        sum_list.add(total_val)

    if carry:
        sum_list.add(carry)
    return sum_list


class TestListAdder(unittest.TestCase):
    """Test List Added"""

    def test_single_number_case(self):
        """Test single number list case."""
        list_1 = SinglyLinkedList(7).get_head()
        list_2 = SinglyLinkedList(5).get_head()
        sum_list = add_two_list(list_1, list_2)
        self.assertEqual('[2 -> 1]', str(sum_list))

    def test_diff_length_case(self):
        """"Test different lenght list case."""
        values_1 = [7, 1]
        values_2 = [5]
        list_1 = SinglyLinkedList(values_1).get_head()
        list_2 = SinglyLinkedList(values_2).get_head()
        sum_list = add_two_list(list_1, list_2)
        self.assertEqual('[2 -> 2]', str(sum_list))

    def test_classic_case(self):
        """Test classic test case"""
        values_1 = [7, 1, 6]
        values_2 = [5, 9, 2]
        list_1 = SinglyLinkedList(values_1).get_head()
        list_2 = SinglyLinkedList(values_2).get_head()
        sum_list = add_two_list(list_1, list_2)
        self.assertEqual('[2 -> 1 -> 9]', str(sum_list))


if __name__ == "__main__":
    unittest.main()
