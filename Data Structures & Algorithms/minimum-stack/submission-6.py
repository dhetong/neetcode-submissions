class MinStack:

    def __init__(self):
        self.stack = []
        self.minnum = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.minnum = val
        else:
            if val >= self.minnum:
                self.stack.append(val-self.minnum)
            else:
                self.stack.append(val-self.minnum)
                self.minnum = val

    def pop(self) -> None:
        num = self.stack.pop()
        if num < 0:
            self.minnum = -1*num +self.minnum

    def top(self) -> int:
        if self.stack[-1] >= 0:
            return self.stack[-1] + self.minnum
        else:
            return self.minnum

    def getMin(self) -> int:
        return self.minnum
