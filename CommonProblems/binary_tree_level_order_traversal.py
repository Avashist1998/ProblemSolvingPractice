"""LC: Binary Tree Level Order Traversal"
from typing import List, Optional

class Node:
	def __init__(self, val: int):
		self.val = val
		self.left: Optional["Node"] = None
		self.right: Optional["Node"] = None


def level_order_traversal(self, root: "Node") -> List[List[int]]:
	
	res = []
	if root is None:
		return res

	queue = [root]
	while queue:
		sub_res = []
		width = len(queue)
		for i in range(width):
			node = queue.pop(0)
			if node:
				sub_res.append(node.val)
				queue.append(node.left)
				queue.append(node.right)
		res.append(sub_res)
	return res[:-1]

