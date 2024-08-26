class Solution:
    def candy(self, ratings: List[int]) -> int:
        leng = len(ratings)
        candies = [0]*leng
        inds = [[ratings[i],i] for i in range(leng)]
        inds.sort()
        ans = 0
        for r,c in inds:
            count = 1
            if  c-1>=0 and r>ratings[c-1] and candies[c-1]>0 and c+1<leng and  r>ratings[c+1] and candies[c+1]>0:
                 count= max(candies[c-1]+1,candies[c+1]+1)
            elif c-1>=0 and r>ratings[c-1] and candies[c-1]>0:
                count= candies[c-1]+1
            elif c+1<leng and  r>ratings[c+1] and candies[c+1]>0:
                count=candies[c+1]+1
            # elif 
            candies[c] = count
            ans+=count
            # print("this is the candies",candies) 
                
        return ans

        