class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [height[0]] * len(height)        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        maxRight = [height[-1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        maxWater = []
        water = 0

        for i in range(len(height)):
            maxWater.append(min(maxLeft[i], maxRight[i]))
            curWater = maxWater[i] - height[i]
            if curWater > 0:
                water += curWater
        
        return water

