#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #topological sort: post order dfs + reverse result
        adj = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            #check invalid prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = set()
        cycle = set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            visited.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            res.append(c)
            return True

        for c in adj:
            if c not in visited:
                if not dfs(c):
                    return ""

        return ''.join(res[::-1])
            
        
# @lc code=end

