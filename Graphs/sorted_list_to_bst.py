from .Node  import binaryTreeNode
from typing import List, Optional



def sorted_list_to_bts(arr:List[int]):

    if len(arr) == 0:
        root = None
    
    elif len(arr) == 1:
        root =  binaryTreeNode(arr[0])

    else:
        middle = len(arr)//2
        root = binaryTreeNode(arr[middle])
        root.left = sorted_list_to_bts(arr[:middle])
        root.right = sorted_list_to_bts(arr[middle+1:])

    return root
