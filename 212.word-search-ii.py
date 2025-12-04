#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rowNum, colNum = len(board), len(board[0])

        result, visited = set(), set() 
        def backtrack(r, c, node, word):
            if (r < 0 or c < 0 or r >= rowNum or c >= colNum or 
                (r,c) in visited or board[r][c] not in node.children):
                return
            

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                result.add(word)

            backtrack(r+1, c, node, word)
            backtrack(r-1, c, node, word)
            backtrack(r, c+1, node, word)
            backtrack(r, c-1, node, word)
            visited.remove((r, c))

        for r in range(rowNum):
            for c in range(colNum):
                backtrack(r, c, root, "")

        return list(result)

        
# @lc code=end

