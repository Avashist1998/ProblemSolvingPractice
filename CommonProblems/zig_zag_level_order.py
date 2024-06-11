from typing import Optional, List

from graphs.tree_node import TreeNode

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    
    if root:
        res = []
        layer = 0
        queue = [root]
        while queue:
            i = 0
            layer_size = len(queue)
            sub_res = []
            while i < layer_size:
                node = queue.pop(0)
                if node:
                    sub_res.append(node.val)
                    queue.append(node.right)
                    queue.append(node.left)
                i += 1
            if layer & 1 == 0:
                sub_res = sub_res[::-1]
            res.append(sub_res)
            layer += 1
        return res[:-1]

    return root
