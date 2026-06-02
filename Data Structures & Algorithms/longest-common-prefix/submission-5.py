class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        print(f"Initial prefix: '{prefix}', len={len(prefix)}")
        
        for s in strs:
            for i in range(len(prefix)):
                if i >= len(s) or s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            print(f"After comparing, prefix: '{prefix}', len={len(prefix)}")
        
        print(f"Final return: '{prefix}'")
        return prefix