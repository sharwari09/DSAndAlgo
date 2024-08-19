# https://leetcode.com/problems/keys-and-rooms/description

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in rooms[node]:
                if n not in visited:
                    dfs(n)
        dfs(0)
        return len(visited) == len(rooms)

"""
Time Complexity: O(N), where N is no. of rooms.
Space Complexity: O(N), where N is no. of rooms.
"""
