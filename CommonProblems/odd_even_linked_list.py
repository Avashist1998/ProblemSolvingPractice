
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def odd_even_linked_list(head: "ListNode") -> "ListNode":


    if head is None:
        return head

    count = 1
    walker = head

    while walker.next:
        walker = walker.next
        count += 1

    if count < 3:
        return head
    
    start = head

    for i in range(count//2):

        walker.next = start.next
        start.next = start.next.next
        walker = walker.next
        start = start.next
        walker.next = None

    return head


"""

A -> B -> C -> D

count = 3
start = A
walker = C

C => B
A => C
walker = B
B.next = None

A -> C -> B


"""