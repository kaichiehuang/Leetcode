#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Codec:

    delim = '%'

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + self.delim + s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        start = 0

        while start < len(s):
            delim_index = s.find(self.delim, start)
            length = int(s[start:delim_index])
            string_start = delim_index + 1
            string_end = string_start + length
            res.append(s[string_start:string_end])
            start = string_end

        return res
            


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

