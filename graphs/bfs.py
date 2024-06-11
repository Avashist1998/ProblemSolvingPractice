from node import node
from collections import deque

"""
class node:
    def __init__(self, val: "node", neighbors: List[Optional["node"]] = []):
        self.val = val
        self.neighbors: List[Optional["node"]] = neighbors

"""


def bfs(root: "node"):
    """Simple queue based Breadth First Search Implementation
    
    Args:
        root: entry node into the graph
    """
    queue = deque()
    queue += [root]
    visited = set()
    while queue:
        node = queue.popleft()
        
        """
        Add work here
        """
        print(node)
        for neigh in node.neighbors:
            if neigh not in visited:
                queue.append(neigh)
        visited.add(node)
    return

