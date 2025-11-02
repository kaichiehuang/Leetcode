#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True
        return

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.eow

            c = word[index]
            if c == '.':
                for key in node.children:
                    if dfs(node.children[key], index + 1):
                        return True
                return False

            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], index + 1)

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

