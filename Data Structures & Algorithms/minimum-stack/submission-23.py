class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            print('adding', val, 'to minStack', self.minStack)
            self.minStack.append(val)
        self.stack.append(val)
        print(val, self.minStack)

    def pop(self) -> None:
        if self.top() == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
