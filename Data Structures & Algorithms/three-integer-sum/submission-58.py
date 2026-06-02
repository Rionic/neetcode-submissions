class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        # [-3, -3, -2, -1, 0, 1, 1, 3, 4]
        target = 0
        while target + 1 < len(nums) - 1:
            first = target + 1
            last = len(nums) - 1
            while first < last:
                triplet = [nums[target], nums[first], nums[last]]
                if nums[first] + nums[last] > -nums[target]:
                    last -= 1
                    continue
                elif nums[first] + nums[last] < -nums[target]:
                    first += 1
                    continue
                elif triplet not in triplets: # Triplet found
                    triplets.append(triplet)
                first += 1
            if triplets: # Skip duplicate target e.g. [-3, -3, -3, 0, 1]
                target += 1
                while target < len(nums) -1 and triplets[-1][0] == nums[target]:
                    target += 1
            else:
                target += 1
        return triplets


