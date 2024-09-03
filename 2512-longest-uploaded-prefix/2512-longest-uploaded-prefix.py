class LUPrefix:

    def __init__(self, n: int):
        self.pre =[False]*(n+2)
        self.ln = 0 
    def upload(self, video: int) -> None:
        self.pre[video-1] = True
        while self.pre[self.ln]:
            self.ln+=1
    def longest(self) -> int:
        return self.ln
        



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()