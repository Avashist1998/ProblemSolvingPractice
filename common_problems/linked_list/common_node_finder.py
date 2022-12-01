"""Find the common node between two linked lists."""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList, SinglyListNode


def find_common_node(list_1: ListNode, list_2: ListNode) -> Optional[ListNode]:
    """Find the common node two linked list.
    Args:
        list_1: head node of the linked list.
        list_2: head node of the linked list.
    Returns:
        node shared by both lists.
    """
    walker_1: Optional[ListNode] = list_1
    walker_2: Optional[ListNode] = list_2

    if walker_1 == walker_2:
        return walker_1
    len_of_list_1 = 0
    while walker_1:
        len_of_list_1 += 1
        walker_1 = walker_1.get_next()
    len_of_list_2 = 0
    while walker_2:
        len_of_list_2 += 1
        walker_2 = walker_2.get_next()

    if len_of_list_1 == 0 or len_of_list_2 == 0:
        return None

    if len_of_list_2 < len_of_list_1:
        list_1, list_2 = list_2, list_1
        len_of_list_1, len_of_list_2 = len_of_list_2, len_of_list_1

    walker_1 = list_1
    walker_2 = list_2
    for _ in range(len_of_list_2 - len_of_list_1):
        if walker_2:
            walker_2 = walker_2.get_next()

    while walker_1 and walker_2:
        if walker_1 == walker_2:
            return walker_1
        walker_1 = walker_1.get_next()
        walker_2 = walker_2.get_next()

    return None


class TestFindCommonNode(unittest.TestCase):
    """Test find_common_node function."""

    def test_root_node_case(self):
        """Test root common node case"""
        values = ["a", "b", "c", "d"]
        node_1 = node_2 = SinglyLinkedList(values).get_head()
        self.assertEqual(node_1, find_common_node(node_1, node_2))

    def test_last_case(self):
        """Test last common node case"""
        node_1 = SinglyLinkedList(["a", "b", "c"]).get_head()
        node_2 = SinglyLinkedList(["e", "d"]).get_head()
        walker_1 = node_1
        walker_2 = node_2
        for _ in range(1):
            walker_1 = walker_1.get_next()
            walker_2 = walker_2.get_next()
        walker_1 = walker_1.get_next()
        walker_2.set_next(walker_1)
        self.assertEqual(walker_1, find_common_node(node_1, node_2))

    def test_middle_node_case(self):
        """Test middle common node case"""
        node_1 = SinglyLinkedList(["a", "b", "c"]).get_head()
        node_2 = SinglyLinkedList(["e", "d"]).get_head()
        walker_1 = node_1
        walker_2 = node_2
        for _ in range(1):
            walker_1 = walker_1.get_next()
            walker_2 = walker_2.get_next()
        walker_1 = walker_1.get_next()
        walker_2.set_next(walker_1)
        walker_2 = walker_2.get_next()
        for char in ["f", "g", "h"]:
            walker_2.set_next(SinglyListNode(char))
            walker_2 = walker_2.get_next()
        self.assertEqual(walker_1, find_common_node(node_1, node_2))

    def test_different_length_case(self):
        """Test different length node case"""
        node_1 = SinglyLinkedList(["a", "b", "c"]).get_head()
        node_2 = SinglyLinkedList(["e"]).get_head()
        walker_1 = node_1
        walker_2 = node_2
        for _ in range(1):
            walker_1 = walker_1.get_next()
        walker_1 = walker_1.get_next()
        walker_2.set_next(walker_1)
        walker_2 = walker_2.get_next()
        for char in ["f", "g", "h"]:
            walker_2.set_next(SinglyListNode(char))
            walker_2 = walker_2.get_next()
        self.assertEqual(walker_1, find_common_node(node_1, node_2))


if __name__ == "__main__":
    unittest.main()
