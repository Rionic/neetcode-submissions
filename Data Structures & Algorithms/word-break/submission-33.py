class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dp array = whether we have a valid string ending at i
        # "applepenapple", wordDict = ["apple","pen","ape"]
        #  j   i      
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):

            for j in range(i, -1, -1):
                # print('s',s[j], s[j:i + 1])
                if s[j:i + 1] in wordDict and dp[j] == True:
                    dp[i + 1] = True
        # print(dp)
        return dp[-1]