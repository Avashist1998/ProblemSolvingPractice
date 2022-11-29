"""Natural Merge Sort Implementation"""

from typing import List, Optional
from algorithms.sorting.base import SortingAlgo
from data_structures.linked_list.base import ListNode
from data_structures.linked_list.singly_linked_list import SinglyLinkedList, SinglyListNode


class NaturalMergeSort(SortingAlgo):
    """MergeSort Algorithm implementation"""

    def __init__(self):
        """Default constructor"""

    def merge_routine(self, list_1: ListNode,
                      list_2: ListNode) -> Optional[ListNode]:
        """Merge routine of the generated files.
        Args:
            list_1: a sorted linked list
            list_2: a sorted linked list
        Returns:
            a sorted linked list by combining inputs
        """
        dummy_head: ListNode = SinglyListNode(0)
        walker = dummy_head
        while list_1 or list_2:

            if list_1 is None:
                assert list_2 is not None
                walker.set_next(list_2)
                list_2 = list_2.get_next()
                walker = walker.get_next()

            elif list_2 is None:
                assert list_1 is not None
                walker.set_next(list_1)
                list_1 = list_1.get_next()
                walker = walker.get_next()

            else:
                if list_1.get_val() > list_2.get_val():
                    walker.set_next(list_2)
                    list_2 = list_2.get_next()
                else:
                    walker.set_next(list_1)
                    list_1 = list_1.get_next()
                walker = walker.get_next()

        return dummy_head.get_next()

    def natural_split_list(self, head: ListNode) -> List[ListNode]:
        """Naturally Splits the Linked List
        Args:
            head: head of the linked list
        Returns:
            Queue of the split nodes
        """
        queue: List[ListNode] = []
        walker: Optional[ListNode] = head
        curr_head: ListNode = head
        while walker:
            if walker.get_next() is None:
                # assert walker.get_next() is None
                queue.append(curr_head)
                walker.set_next(None)
                walker = walker.get_next()

            elif walker.get_next().get_val() < walker.get_val():
                queue.append(curr_head)
                curr_head = walker.get_next()
                walker.set_next(None)
                walker = curr_head

            else:
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
            len_queue = len(queue)
            while len_queue != 1:
                while len_queue > 0:
                    if len_queue > 1:
                        list_1 = queue.pop(0)
                        list_2 = queue.pop(0)
                        len_queue -= 2
                        merged_list = self.merge_routine(list_1, list_2)
                        assert merged_list is not None
                        queue.append(merged_list)
                    else:
                        queue.append(queue.pop(0))
                        len_queue -= 1
                len_queue = len(queue)

            res = []
            walker = queue.pop(0)
            while walker:
                res.append(walker.get_val())
                walker = walker.get_next()
            return res
        return []
