class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]

        l = 0
        r = len(values) - 1
        greatest = ""

        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                greatest = values[m][1] # largest key w/ t <= timestamp so far
                l = m + 1
            else:
                r = m - 1

        return greatest
