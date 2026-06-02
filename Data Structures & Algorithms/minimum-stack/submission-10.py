class MinStack:

    def __init__(self):
        self.s = []
        self.sMin = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.sMin or val <= self.sMin[-1]:
            self.sMin.append(val)
        
    def pop(self) -> None:
        if self.sMin[-1] == self.s[-1]:
            self.sMin.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.sMin[-1]
        
