#https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i: [] for i in range(n)}
        incoming = {i: 0 for i in range(n)}

        for dest, src in prerequisites:
            adjlist[src].append(dest)
            incoming[dest] += 1
        ans = []
        queue = deque([])
        for course, degree in incoming.items():
            if degree == 0:
                queue.append(course)
                ans.append(course)
        while queue:
            course = queue.popleft()
            for child in adjlist[course]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
                    ans.append(child)

        return ans if len(ans) == n else []


"""
Time Complexity: O(N), where n is the no. courses
Space Complexity: O(N), where n is the no. courses
"""
