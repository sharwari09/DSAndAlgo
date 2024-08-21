# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def topView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root, 0])
        ans = defaultdict(int)
        while queue:
            l = len(queue)
            for i in range(l):
                node, col = queue.popleft()
                if col not in ans: # Only difference between top view and bottom view. 
                    ans[col] = node.val 
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append(node.right, col+1)
        return ans.values()

"""
Time Complexity: O(N), N is the no. of nodes
Space Complexity: O(N), N is the no. of nodes
"""
