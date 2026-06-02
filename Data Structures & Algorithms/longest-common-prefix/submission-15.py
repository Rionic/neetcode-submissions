class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        # ["bat","bag","bank","band"]
        #  "bat"
        for s in strs:
            for i in range(len(prefix)):
                if i >= len(s) or s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        
        return prefix
                    
            
        