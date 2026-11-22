class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nmap = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in nmap:
                return [nmap[nums[i]], i]
            nmap[target - nums[i]] = i
        
