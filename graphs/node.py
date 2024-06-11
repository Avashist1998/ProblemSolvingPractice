from typing import List, Optional

class node:
    """Definition of a graph node """
    def __init__(self, val: "node", neighbors: List[Optional["node"]] = []):
        """Constructor function for the node"""
        self.val = val
        self.neighbors: List[Optional["node"]] = neighbors
