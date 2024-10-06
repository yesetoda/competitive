class MyCalendarTwo:

    def __init__(self):
        self.one = []
        self.two = []
    def book(self, start: int, end: int) -> bool:
        for ts,te  in self.two:
            tovs,tove = max(start,ts),min(end,te)
            if tovs<tove:
                return False
        for os,oe in self.one:
            oovs,oove =  max(start,os),min(end,oe)
            if oovs<oove:
                self.two.append([oovs,oove])
        self.one.append([start,end])
        return True


        



