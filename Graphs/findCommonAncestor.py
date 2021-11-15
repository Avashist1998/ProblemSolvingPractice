

# You are given a binary tree root node
# you are give two nodes 
# you need to return the closest ancestor 



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    
    def dfs(root: 'TreeNode', node:'TreeNode', path:list) -> bool:
            
            if root == node:
                return True
                
            
            else:
                
                val = dfs.append(root.right, node, path)
                if val:
                    path.append(root.right)
                    return val
                
                val = dfs.append(root.left, node, path)
                if val:
                    path.append(root.left)
                    return val
                
    if root == p or root == q:
        return root
    
    else:
        p_path = list()
        p_path.append(root.val)
        
        q_path = list()
        q_path.append(root.val)
        dfs(root, p, p_path)
        dfs(root, q, q_path)
        
        res = root 
        
        for i in range(min(len(q_path), len(p_path)) - 1):
            res = q_path[i]
            if q_path[i+1] != p_path[i+1]:
                return res