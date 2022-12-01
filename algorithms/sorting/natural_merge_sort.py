"""Natural Merge Sort Implementation"""

from typing import List, Optional
from algorithms.sorting.base import SortingAlgo
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList, SinglyListNode


class NaturalMergeSort(SortingAlgo):
    """MergeSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def merge_routine(self, list_1: Optional[ListNode],
                      list_2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge routine of the generated files.
        Args:
            list_1: a sorted linked list
            list_2: a sorted linked list
        Returns:
            a sorted linked list by combining inputs
        """
        dummy_head: ListNode = SinglyListNode(0)
        walker: Optional[ListNode] = dummy_head
        while list_1 or list_2:

            if list_1 is None:
                assert list_2 is not None
                assert walker is not None
                walker.set_next(list_2)
                list_2 = list_2.get_next()
                walker = walker.get_next()

            elif list_2 is None:
                assert list_1 is not None
                assert walker is not None
                walker.set_next(list_1)
                list_1 = list_1.get_next()
                walker = walker.get_next()

            else:
                if list_1.get_val() > list_2.get_val():
                    assert walker is not None
                    walker.set_next(list_2)
                    list_2 = list_2.get_next()
                else:
                    assert walker is not None
                    walker.set_next(list_1)
                    list_1 = list_1.get_next()
                walker = walker.get_next()

        return dummy_head.get_next()

    def natural_split_list(self, head: ListNode) -> List[Optional[ListNode]]:
        """Naturally Splits the Linked List
        Args:
            head: head of the linked list
        Returns:
            Queue of the split nodes
        """
        queue: List[Optional[ListNode]] = []
        walker: Optional[ListNode] = head
        curr_head: Optional[ListNode] = head
        while walker:
            walker_next = walker.get_next()
            if walker_next:
                if walker_next.get_val() < walker.get_val():
                    queue.append(curr_head)
                    curr_head = walker.get_next()
                    walker.set_next(None)
                    walker = curr_head
                else:
                    walker = walker_next
            else:
                queue.append(curr_head)
                walker.set_next(None)
                walker = walker.get_next()
        return queue

    def sort(self, arr: List[int]) -> List[int]:
        """Merge sorting method.
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Args:
            arr: List containing integers.
        Returns:
            sorted list of integers.
        """

        arr_linked_list = SinglyLinkedList(arr)
        if arr_linked_list.get_head() is not None:
            assert arr_linked_list.get_head() is not None
            arr_head: Optional[ListNode] = arr_linked_list.get_head()
            assert arr_head is not None
            queue = self.natural_split_list(arr_head)
            while len(queue) > 1:
                list_1 = queue.pop(0)
                list_2 = queue.pop(0)
                merged_list = self.merge_routine(list_1, list_2)
                assert merged_list is not None
                queue.append(merged_list)

            res = []
            walker: Optional[ListNode] = queue.pop(0)
            while walker:
                res.append(walker.get_val())
                walker = walker.get_next()
            return res
        return []
