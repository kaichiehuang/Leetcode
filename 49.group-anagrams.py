#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resDict = defaultdict(list)
        for str in strs:
            # Use sorted string as key (hashable)
            key = ''.join(sorted(str))
            resDict[key].append(str)
        
        return list(resDict.values())



# @lc code=end

