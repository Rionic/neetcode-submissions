class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        start, end = 0, 0
        tank = 0
        n = len(gas)
        for _ in range(n):
            if tank >= 0:
                tank += gas[end] - cost[end]
                end = (end + 1) % n 
            else:
                start = (start - 1) % n
                tank += gas[start] - cost[start]

        return start

