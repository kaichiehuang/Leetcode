#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0],0,0]] #height, r, c
        visited = set()

        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            if (r, c) == (N-1, N-1):
                return h
            visited.add((r, c))
            dir = [[1,0],[-1, 0],[0, 1],[0, -1]]
            for dr, dc in dir:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row >= N or col >= N or (row, col) in visited:
                    continue
                visited.add((row, col)) #optimization works because
                heapq.heappush(minHeap, [max(h, grid[row][col]), row, col])
        
        




# @lc code=end

