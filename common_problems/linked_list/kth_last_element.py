"""Returns the Kth last element"""

from typing import Optional
import unittest
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList


def find_k_th_last_node(head: ListNode, k: int) -> Optional[ListNode]:
    """Finds the Kth last node in the list.
    Args:
        head: head node of the list.
        k: the placement of the node from the back.
    Returns:
        K th node from the back of the list.
    """
    walker: Optional[ListNode] = head
    k_node: Optional[ListNode] = head
    for _ in range(k):
        if walker is None:
            return walker
        assert walker is not None
        walker = walker.get_next()

    while walker:
        assert walker is not None
        assert k_node is not None
        walker = walker.get_next()
        k_node = k_node.get_next()
    return k_node


class TestKthNodeFinder(unittest.TestCase):
    """Test the find_k_th_last_node function"""

    def test_different_k_values(self):
        """Test find_k_th_last_node function of different value of k"""

        values = [1, 2, 4, 2, 6, 8, 14, 28, 25, 19, 12]
        linked_list = SinglyLinkedList(values).get_head()
        self.assertEqual(12, find_k_th_last_node(linked_list, 1).get_val())
        self.assertEqual(19, find_k_th_last_node(linked_list, 2).get_val())
        self.assertIsNone(find_k_th_last_node(linked_list, 20))


if __name__ == "__main__":
    unittest.main()
