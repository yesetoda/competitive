class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        x = []
        for i in arr:
            if i<0:
                x.append((k-((-i)%k))%k)
            else:
                x.append(i%k)
        x.sort()
        ind = 0
        while ind <len(x):
            left = bisect_left(x,x[ind])
            right = bisect_right(x,x[ind])
            if x[ind] == 0:
                if (right - left)%2:
                    return False
            else:
                mate_left = bisect_left(x,k-x[ind])
                mate_right = bisect_right(x,k-x[ind])

                if right-left != mate_right-mate_left:
                    return False
            ind = right
        return True
            

