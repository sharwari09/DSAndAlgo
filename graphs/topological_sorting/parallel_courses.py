# https://leetcode.com/problems/parallel-courses

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjlist = {i : [] for i in range(1, n+1)}
        incoming = {i : 0 for i in range(1, n+1)}

        for src, dest in relations:
            adjlist[src].append(dest)
            incoming[dest] += 1
        
        queue = deque([])
        courses = 0
        for node, edges in incoming.items():
            if edges == 0:
                queue.append((node, 1))
                courses += 1
        semester = 0
        while queue:
            course, semester = queue.popleft()
            for nei in adjlist[course]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    queue.append((nei, semester+1))
                    courses += 1
        return semester if courses == n else -1

"""
Time Complexity: O(N), where n is the no. courses
Space Complexity: O(N), where n is the no. courses
"""
