# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bottomView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root, 0])
        ans = defaultdict(int)
        ans[0] = root.val
        while queue:
            l = len(queue)
            for i in range(l):
                node, col = queue.popleft()
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append(node.right, col+1)
        return ans