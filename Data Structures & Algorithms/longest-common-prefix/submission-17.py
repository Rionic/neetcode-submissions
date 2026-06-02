class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            i = 0
            while i < len(s) and i < len(prefix) and s[i] == prefix[i]:
                i += 1
            prefix = prefix[:i]
            # for i in range(len(prefix)):
            #     if i >= len(s) or s[i] != prefix[i]:
            #         prefix = prefix[:i]
            #         break
        
        return prefix
                    
            
        