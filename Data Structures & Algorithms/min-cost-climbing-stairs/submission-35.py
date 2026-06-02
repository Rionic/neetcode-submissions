class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # total[i] = min(cost[i] + total[i-2], cost[i] + total[i-1])
        one = two = 0
        for i in range(len(cost)):
            three = min(cost[i] + two, cost[i] + one)
            one = two
            two = three

        return min(one, two)
