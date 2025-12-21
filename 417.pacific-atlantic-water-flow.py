#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #backwards, find all cells reachable from each ocean and find intersection
        pacificSeen = set()
        atlanticSeen = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, seenSet, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seenSet or heights[r][c] < prevHeight:
                return

            seenSet.add((r, c))
            dirs = [[1,0],[-1, 0],[0, 1],[0, -1]]
            for dx, dy in dirs:
                row, col = r + dx, c + dy
                dfs(row, col, seenSet, heights[r][c])
            
            return

        for c in range(COLS):
            #pacific
            dfs(0, c, pacificSeen, -1)
            #atlantic
            dfs(ROWS-1, c, atlanticSeen, -1)

            
        for r in range(ROWS):
            dfs(r, 0, pacificSeen, -1)
            dfs(r, COLS-1, atlanticSeen, -1)

        return [list(cell) for cell in pacificSeen.intersection(atlanticSeen)]


# @lc code=end

