# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.adj_list = {i: [] for i in range(-1, n)}
        for emp in range(n):
            self.adj_list[manager[emp]].append(emp)
        self.time = 0
        self.dfs(informTime, headID, informTime[headID])
        return self.time

    def dfs(self, informTime, manager, time):
        if len(self.adj_list[manager]) == 0:
            self.time = max(self.time, time)
        for emp in self.adj_list[manager]:
            self.dfs(informTime, emp, time+informTime[emp])

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
