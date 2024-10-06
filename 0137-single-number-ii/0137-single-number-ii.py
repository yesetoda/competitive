class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0]*32
        negs = [0]*32
        for i in nums:
            val = i
            ind = 0
            negative = False
            if val<0:
                val = abs(val)
                negative = True
            while val>0:
                if val&1 == 1:
                    if negative:
                        negs[ind]+=1
                    else:
                        bits[ind]+=1
                val>>=1
                ind+=1
        pos = 0
        for i in range(32):
            if bits[i]%3:
                pos+=2**i
        neg = 0
        for i in range(32):
            if negs[i]%3:
                neg-=2**i
        # print(pos,neg)
        if pos == 0:
            return neg
        return pos


