#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #key insight: bfs, rotting happens at multiple location at the same time
        q = deque()
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dir:
                    row = r + dr
                    col = c + dc
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1

# @lc code=end

