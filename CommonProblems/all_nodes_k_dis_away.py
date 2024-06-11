# LC 863. All Nodes Distance K in Binary Tree
from typing import List, Dict
from graphs.tree_node import TreeNode

def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """"""
    def get_k_level(root: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [root.val]

        res = []
        queue = [(root, 0)]
        while queue:
            node, dis = queue.pop()
            if dis == k:
                res.append(node.val)
            else:
                if node.left:
                    queue.append((node.left, dis+1))
                if node.right:
                    queue.append((node.right, dis+1))

        return res

    def restructure(node: TreeNode, look_up: Dict[TreeNode, TreeNode]):
        """Restructure the tree to make the node the root and all parents as children."""
        new_root = node
        while node in look_up and look_up[node] is not None:
            if node.left is None:
                parent = look_up[node]
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                node.left = parent
            else:
                parent = look_up[node]
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                node.right = parent
            node = parent
        return new_root

    queue = [(root, None)]
    child_to_parent_map = {}
    node = None
    parent = None
    while queue:
        node, parent = queue.pop(0)
        child_to_parent_map[node] = parent
        if node is target:
            queue = []
        else:
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))


    res = get_k_level(node, k)
    if parent and k != 0:
        if parent.left is not None and parent.left is node:
            parent.left = None
        else:
            parent.right = None
        parent = restructure(parent, child_to_parent_map)
        top = get_k_level(parent, k-1)
        res += top
    
    return res



