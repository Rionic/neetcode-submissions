class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)

        for i, num in enumerate(numbers):
            numMap[num] = (target - num, i+1)
        print(numMap)
        for key in numMap:
            if numMap[key][0] in numMap:
                return [numMap[key][1], numMap[numMap[key][0]][1]]

        