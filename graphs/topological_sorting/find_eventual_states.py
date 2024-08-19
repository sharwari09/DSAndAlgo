# https://leetcode.com/problems/find-eventual-safe-states

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        l = len(graph)
        res = {}
        for index in range(l):
            self.dfs(graph, res, index)
        for index in range(l):
            if res[index]:
                ans.append(index)
        return ans

    def dfs(self, graph, res, node):
        if node in res:
            return res[node]
        res[node] = False
        for nei in graph[node]:
            if not self.dfs(graph, res, nei):
                return False
        res[node] = True
        return True

"""
Time Complexity: O(N), where N is the no. of nodes
Space Complexity: O(N), where N in the no. of nodes
"""
