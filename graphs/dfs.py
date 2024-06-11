from node import node
"""
class node:
    def __init__(self, val: "node", neighbors: List[Optional["node"]] = []):
        self.val = val
        self.neighbors: List[Optional["node"]] = neighbors
"""


def dfs(root: "node"):
    """Simple queue based Breadth First Search Implementation
    
    Args:
        root: entry node into the graph
    """
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop(-1)
        """
        Add work here
        """
        print(node)
        for neigh in node.neighbors:
            if neigh not in visited:
                stack.append(neigh)
        visited.add(node)
    return

