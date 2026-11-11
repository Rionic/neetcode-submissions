class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.perms = []
        self.used = set()
        def dfs(perm):
            if len(perm) == n:
                self.perms.append(perm.copy())
                return

            for j in range(n):
                if nums[j] in self.used:
                    continue
                self.used.add(nums[j])
                dfs(perm + [nums[j]])
                self.used.remove(nums[j])

        dfs([])

        return self.perms