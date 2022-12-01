"""Partition a list based on value."""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def partition_list(node: ListNode, val: int) -> Optional[ListNode]:
    """Partition the list based on the value.
    Args:
        val: int value to split the list
        node: head of the linked list
    Returns:
        head node of a list with the partition across the value
    """
    left_list: SinglyLinkedList = SinglyLinkedList()
    right_list: SinglyLinkedList = SinglyLinkedList()

    walker: Optional[ListNode] = node
    while walker:

        if int(walker.get_val()) > val:
            right_list.add(walker.get_val())
        else:
            left_list.add(walker.get_val())
        walker = walker.get_next()

    for right in right_list:
        left_list.add(right.get_val())

    return left_list.get_head()


class TestPartitionList(unittest.TestCase):
    """Test partition_list function."""

    def test_middle_partition_case(self):
        """Test middle partition case"""
        values = [1, 5, 8, 2, 7, 3]
        final_values = [1, 2, 3, 5, 8, 7]
        node = SinglyLinkedList(values).get_head()
        partition_node = partition_list(node, 3)
        for value in final_values:
            # print(f"value : {value}, node_value: {partition_node.get_val()}")
            self.assertEqual(value, partition_node.get_val())
            if partition_node:
                partition_node = partition_node.get_next()

    def test_all_left_case(self):
        """Test all left partition case"""
        values = [1, 5, 8, 2, 7, 3]
        node = SinglyLinkedList(values).get_head()
        partition_node = partition_list(node, 9)
        for value in values:
            self.assertEqual(value, partition_node.get_val())
            if partition_node:
                partition_node = partition_node.get_next()

    def test_all_right_case(self):
        """Test all right partition case"""
        values = [1, 5, 8, 2, 7, 3]
        node = SinglyLinkedList(values).get_head()
        partition_node = partition_list(node, 1)
        for value in values:
            self.assertEqual(value, partition_node.get_val())
            if partition_node:
                partition_node = partition_node.get_next()


if __name__ == "__main__":
    unittest.main()
