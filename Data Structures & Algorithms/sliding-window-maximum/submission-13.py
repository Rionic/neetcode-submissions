class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([0])
        max_list = []

        for i in range(1, k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        max_list.append(nums[q[0]])
        # [1,2,1,0,4,2,6], k = 3
        #          L   i
        # [2,2,4,4,6]
        # [6]
        for i in range(k, len(nums)):
            if nums[i] >= nums[q[-1]]:
                # Why this check? If we have a number greater q[-1]
                # That means this new number will always be chosen as max
                # and that we do not need q[-1] as it is smaller. Pop & repeat
                while q and nums[i] > nums[q[-1]]:
                    q.pop()
            q.append(i)
            # i - k is L side of window
            if q[0] <= i - k: # Window has moved past this element. pop it
                q.popleft()
            # print(q, i-k)
            max_list.append(nums[q[0]])
            

        return max_list

        
        
