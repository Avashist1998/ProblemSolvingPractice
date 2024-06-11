# LC 24.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    """

    if head is None:
        return head
    elif head.next is None:
        return head

    queue = []
    walker = head
    while walker and walker.next:
        tmp = walker.next
        walker.next = walker.next.next
        queue.append(tmp)
        walker = walker.next

    walker = head
    head = queue[0]
    while queue:
        node = queue.pop(0)
        node.next = walker
        walker = walker.next
        if queue:
            node.next.next = queue[0]
        else:
            node.next.next = None
    if walker:
        node.next.next = walker
    return head
