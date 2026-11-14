class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        i, start = 0, 0
        n = len(gas)
        j = 0
        while 1:
            j += 1
            tank = gas[i] - cost[i]
            # print('start at', start, tank)
            while tank >= 0:
                i = (i + 1) % n 
                tank += gas[i] - cost[i]
                if start == i:
                    return start
            # i is where we had neg tank. if we dec start, we could find spots w more fuel
            # start -> i-1 is a range where we have tank > 0. 
            start = (start - 1) % n
            i = start

