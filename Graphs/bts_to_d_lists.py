from .Node  import binaryTreeNode
from typing import List, Optional
from LinkedList.LinkedList import node




def bts_to_d_lists(root:binaryTreeNode):
    # breadth first treversal 
    res = list()
    
    if root == None:
        return res

    queue = [root]
    
    walker = None

    while(len(queue)):
        count = len(queue)
        
        for i in range(queue):
            pointer = queue.pop(0)
            if walker == None:
                head = node(pointer.val)
                walker = head
            else:
                walker.next_node = node(pointer.val)
                walker = walker.next 
            
            if pointer.left:
                queue.append(pointer.left)
            if pointer.right:
                queue.append(pointer.right)
        walker = None 
        res.append(head)
