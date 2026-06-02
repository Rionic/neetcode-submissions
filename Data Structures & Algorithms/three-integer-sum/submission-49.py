class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        for i in range(len(nums)):
            target = -nums[i]
            seen = set()

            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    triplet = sorted([nums[i], nums[j], complement])
                    if triplet not in triplets:
                        triplets.append(triplet)

                seen.add(nums[j])
        
        return triplets
