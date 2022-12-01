"""Delete the middle node."""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def delete_middle_node(head: ListNode) -> ListNode:
    """Deletes the middle node a linked list.
    Args:
        head: head node of the linked list.
    Returns:
        head of the list with the middle node removed.
    """
    len_of_list = 0
    walker: Optional[ListNode] = head
    while walker:
        len_of_list += 1
        walker = walker.get_next()

    walker = head
    nodes_to_middle = int(len_of_list // 2) - 1
    while nodes_to_middle > 0:
        nodes_to_middle -= 1
        if walker:
            walker = walker.get_next()
    if walker:
        walker_next = walker.get_next()
        if walker and walker_next:
            walker.set_next(walker_next.get_next())
    return head


class TestDeleteMiddleNode(unittest.TestCase):
    """Test delete_middle_node function."""

    def test_empty_list_case(self):
        """Test empty list case"""
        node = SinglyLinkedList().get_head()
        self.assertIsNone(delete_middle_node(node))

    def test_one_item_list_case(self):
        """Test one item list case"""
        node = SinglyLinkedList("a").get_head()
        self.assertEqual(node, delete_middle_node(node))

    def test_two_item_list_case(self):
        """Test two item list case"""
        values = ["a", "b"]
        node = SinglyLinkedList(values).get_head()
        self.assertEqual(node, delete_middle_node(node))
        len_of_new_list = 0
        while node:
            len_of_new_list += 1
            node = node.get_next()
        self.assertEqual(len_of_new_list, len(values) - 1)

    def test_three_item_list_case(self):
        """Test three item list case"""
        values = ["a", "b", "c"]
        node = SinglyLinkedList(values).get_head()
        self.assertEqual(node, delete_middle_node(node))
        walker, len_of_new_list = node, 0
        while walker:
            len_of_new_list += 1
            walker = walker.get_next()
        self.assertEqual(len_of_new_list, len(values) - 1)

        walker = node
        for char in ["a", "c"]:
            if walker:
                self.assertEqual(char, walker.get_val())
            walker = walker.get_next()

    def test_four_item_list_case(self):
        """Test four item list case"""
        values = ["a", "b", "c", "d"]
        node = SinglyLinkedList(values).get_head()
        self.assertEqual(node, delete_middle_node(node))
        walker, len_of_new_list = node, 0
        while walker:
            len_of_new_list += 1
            walker = walker.get_next()
        self.assertEqual(len_of_new_list, len(values) - 1)

        walker = node
        for char in ["a", "b", "d"]:
            if walker:
                self.assertEqual(char, walker.get_val())
            walker = walker.get_next()


if __name__ == "__main__":
    unittest.main()
