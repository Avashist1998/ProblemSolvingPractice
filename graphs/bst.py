from tree_node import TreeNode


class BST:

    def __init__(self):
        """
            Constructor:
        """

        self.root = None
    
    def insert(self, val: int):
        """
            Insert a value in the tree
        """

        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node: TreeNode, new_node: TreeNode):
        """
            Recursive insert
        """
        if new_node.val <= node.val:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, new_node)


    def delete(self, val: int) -> bool:
        """
            Delete a value from the tree
        """
        if self.root:
            if self.root.val == val:
                if self.root.left is not None and self.root.right is not None:
                    left = self.root.left
                    right = self.root.right
                    self.root = right
                    self._insert(self.root, left)
            return self._delete(self.root, val)
        return False

    def _delete(self, node: TreeNode, val: int) -> bool:
        """
            Recursive delete
        """
        if node is None:
            return False

        if node.left != None:
            if node.left.val == val:
                left = node.left
                node.left = left.left
                if node.right is None:
                    node.right = left.right
                else:
                    self._insert(node.right, left.right)
                return True
            else:
                return self._delete(node.left, val)
        else:
            if node.right.val == val:
                right = node.right
                node.right = right
                if node.left is None:
                    node.left = right.left
                else:
                    self._insert(node.left, right.left)
                return True
            else:
                return self._delete(node.right, val)
    

    # def _delete(self, node: TreeNode, val: int):
    #     """
    #         Recursive delete
    #     """
    #     if node is None:
    #         return

    #     if node.left != None:
    #         if node.left.val == val:
    #             left = node.left
    #             node.left = left.left
    #             if node.right is None:
    #                 node.right = left.right
    #             else:
    #                 self._insert(node.right, left.right)
    #         else:
    #             self._delete(node.left, val)
    #     else:
    #         if node.right.val == val:
    #             right = node.right
    #             node.right = right
    #             if node.left is None:
    #                 node.left = right.left
    #             else:
    #                 self._insert(node.left, right.left)
    #         else:
    #             self._delete(node.right, val)

    

    
