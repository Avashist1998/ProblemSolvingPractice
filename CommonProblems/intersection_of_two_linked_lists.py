# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       
    	w1, w2 = headA, headB
	    step_count_1, step_count_2 = 0, 0
        
        while (w1 or w2):
            if w1:
                w1 = w1.next
                step_count_1 += 1
            if w2:
                w2 = w2.next
                step_count_2 += 1


        diff = abs(step_count_1 - step_count_2)
        
        fast = headA
        slow = headB
        if step_count_2 > step_count_1:
            fast, slow = headB, headA


        for _ in range(diff):
            fast = fast.next


        while (fast and slow):
            
            if (slow == fast):
                return slow
            slow = slow.next
            fast = fast.next
        return None
        
