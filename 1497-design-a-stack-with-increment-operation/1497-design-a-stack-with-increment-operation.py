class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.s = deque()

    def push(self, x: int) -> None:
        if len(self.s)<self.max_size:
            self.s.appendleft([x,0])
            
    def pop(self) -> int:
        val = -1
        increment = 0
        if self.s:
            val,increment = self.s.popleft() 
            if self.s:
                self.s[0][1] += increment
        return val+increment
        

    def increment(self, k: int, val: int) -> None:
        if k>=len(self.s):
            if self.s:
                self.s[0][1] += val
        else:
            self.s[-k][1] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)