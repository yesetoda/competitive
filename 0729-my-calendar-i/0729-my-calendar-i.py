

class MyCalendar:
    def intersect(self,ind,x,y,start,end):
        if x<=start<y:
            return True
        if x<end<y:
            return True
        if start<= x<end:
            return True
        if start<y<end:
            return True
        if ind>0:
            x,y = self.calendar[ind-1]
            if x<=start<y:
                return True
            if x<end<y:
                return True
        return False

    def __init__(self):
        self.calendar = [(-1,-1)]

    def book(self, start: int, end: int) -> bool:
        ind = bisect_left(self.calendar,(start,end))
        if ind <len(self.calendar):
            x,y = self.calendar[ind]
            if self.intersect(ind,x,y,start,end):
                return False
            insort_left(self.calendar,(start,end))
            return True
        else:
            if ind>0:
                x,y = self.calendar[ind-1]
                if  self.intersect(ind,x,y,start,end):
                    return False
                insort_left(self.calendar,(start,end))
                return True
            insort_left(self.calendar,(start,end))
            return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)