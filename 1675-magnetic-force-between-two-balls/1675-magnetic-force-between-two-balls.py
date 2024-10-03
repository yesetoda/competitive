class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        leng = len(position)
        mn = 1
        mx = max(position)
        def find(k):
            # print("this is the k",k)
            ind = 0
            ans = float("inf")
            for i in range(m-1):
                n_ind = bisect_left(position,position[ind]+k)
                if n_ind==leng:
                    return 0
                ans = min(ans,position[n_ind]-position[ind])
                # print(ind,n_ind,ans)
                ind = n_ind
            return ans
        force = 0
        while mn<=mx:
            mid = (mn+mx)//2
            fr = find(mid)
            # print(mid,fr,force)
            if fr==0 or fr < force:
                mx = mid-1
            else:
                mn = mid+1
                force = fr
        return force
            


            

