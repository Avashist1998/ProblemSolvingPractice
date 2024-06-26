# Definition for singly-linked list.
class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        w1, w2 = l1, l2
        carry, num_1, num_2 = 0, 0, 0

        while (carry or w1 or w2):
            
            if w1:
                num_1 = w1.val
            
            if w2:
                num_2 = w2.val
            
            total = carry + num_1 + num_2
            val = total%10
            carry = total//10
            
            w1.val = val
            if w1.next is None and (carry or (w2 and w2.next)):
                w1.next = ListNode(0)
            w1 = w1.next
            
            if w2:
                w2 = w2.next
            num_1, num_2 = 0, 0

        return w1
                  
