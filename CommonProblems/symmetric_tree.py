"""LC: 101 Symmetric Tree """

def Node:
	"""Simple Implimentation of node"""
	def __init__(self, val: int):
		self.val = val
		self.right = None
		self.left = None

def isSymmetric(root: "Node"):
	"""Check weather a tree is symmetric"""
	
	if root is None:
		return True
	
	queue = [[root.left, root.right]]

	while queue:
		l, r = queue.pop()
		if l is None and r is not None:
			return False
		elif r is None and l is not None:
			return False
		elif r is None and l is None:
			pass
		else:
			if r.val != l.val:
				return False
			else:
				queue.append([l.left, r.right])
				queue.append([l.right, r.left])

	return True

