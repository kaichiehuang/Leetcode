#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #key: use BFS
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        INF = 2147483647

        # Add all gates to queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0<=row<ROWS and 0<=col<COLS and rooms[row][col] == INF):
                        rooms[row][col] = rooms[r][c] + 1
                        q.append((row, col))

# @lc code=end