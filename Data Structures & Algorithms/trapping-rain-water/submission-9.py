class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        #              b
        # ml = 3
        # mr = 3
        # water = 9

        if len(height) <= 2: return 0
        
        l, r = 1, len(height) - 2
        maxL, maxR = height[0], height[-1]
        water = 0

        while l <= r:
            maxL = max(maxL, height[l - 1])
            maxR = max(maxR, height[r + 1])
            if maxL <= maxR:
                water += max(0, maxL - height[l])
                l += 1
            else:
                water += max(0, maxR - height[r])
                r -= 1
        
        return water




