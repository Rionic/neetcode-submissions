class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.used = set()
        
        def dfs(perm):
            if len(perm) == len(nums):
                self.perms.append(perm.copy())
                return

            for n in nums:
                if n in self.used:
                    continue
                self.used.add(n)
                dfs(perm + [n])
                self.used.remove(n)

        dfs([])

        return self.perms