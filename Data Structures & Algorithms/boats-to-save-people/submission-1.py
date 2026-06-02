class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        # [1,3,4,8,9], limit 10
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else: # right person is too fat
                r -= 1
            boats +=1

        return boats