class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r=0,len(heights)-1
        maxvol=0

        while l<r:
            maxvol=max(
                maxvol,
                min(heights[l],heights[r]) *
                (r-l)
            )
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return maxvol
