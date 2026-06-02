class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0: return 0
        if len(cost) == 1: return cost[0]
        # totalCost = [0] * len(cost)
        one, two = cost[-1], cost[-2]
        # totalCost[-1] = cost[-1]
        # totalCost[-2] = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            three = min(one, two) + cost[i]
            one = two
            two = three
            # totalCost[i] = cost[i] + min(totalCost[i + 1], totalCost[i + 2])
        return min(one, two)
