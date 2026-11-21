class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def dfs(i, rem):
            if rem == 0:
                return 1
            if (i, rem) in dp:
                return dp[(i, rem)]
            ways = 0

            for j in range(i, len(coins)):
                if rem - coins[j] >= 0:
                    ways += dfs(j, rem - coins[j])

            dp[(i, rem)] =  ways    
            return dp[(i, rem)]

        return dfs(0, amount)