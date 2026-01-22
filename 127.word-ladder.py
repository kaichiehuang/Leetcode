#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        q = deque([beginWord])
        visited = {beginWord}
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in pattern_map[pattern]:
                        if neighbor not in visited:
                            #add to visited immediately to prevent the most duplicates
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0


# @lc code=end

