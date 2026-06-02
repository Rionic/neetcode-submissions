class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        #              b
        # ml = 3
        # mr = 3
        # water = 9

        if len(height) <= 2: return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        
        return water




