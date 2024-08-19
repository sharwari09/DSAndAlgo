# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adjlist = {}
        for employee in employees:
            if employee.id not in adjlist:
                adjlist[employee.id] = employee
        if len(adjlist[id].subordinates) == 0:
            return adjlist[id].importance
        importance = self.dfs(adjlist, adjlist[id], adjlist[id].importance)
        return importance

    def dfs(self, adjlist, employee, importance):
        if len(employee.subordinates) == 0:
            return employee.importance
        local_imp = employee.importance
        for child in adjlist[employee.id].subordinates:
            local_imp += self.dfs(adjlist, adjlist[child], importance+employee.importance)
        return local_imp

"""
Time Complexity: O(N), N is the no. of employees
Space Complexity: O(N), N is the no. of employees
"""
        
        
        
