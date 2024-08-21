# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        left = []
        ans = [root.val]
        cur = root.left
        while cur:
            left.append(cur)
            cur = cur.left or cur.right # Traverse left nodes
          
        right = []
        cur = root.right
        while cur:
            right.append(cur)
            cur = cur.right or cur.left # Traverse right nodes
          
        leaves = []
        stack = [root]
        while stack: # Traverse leaf nodes
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                leaves.append(node)
        
        visited = set([root])
        def visit(node): # Check if any nodes are repeated 
            if node not in visited:
                visited.add(node)
                ans.append(node.val)

        for node in left: visit(node)
        for node in leaves: visit(node)
        for node in reversed(right): visit(node)
            
        return ans # Return combined nodes

"""
Time Complexity: O(N), N is the no. of nodes
Space Complexity: O(N), N is the no. of nodes
"""
