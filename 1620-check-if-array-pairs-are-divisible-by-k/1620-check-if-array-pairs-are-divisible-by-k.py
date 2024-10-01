class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i in range(len(arr)):
            if i<0:
                arr[i] = k - abs(arr[i])%k
            arr[i]= arr[i]%k
        arr.sort()
        ind = 0
        while ind <len(arr):
            left = bisect_left(arr,arr[ind])
            right = bisect_right(arr,arr[ind])
            if arr[ind] == 0:
                if (right - left)%2:
                    return False
            else:
                mate_left = bisect_left(arr,k-arr[ind])
                mate_right = bisect_right(arr,k-arr[ind])
                if right-left != mate_right-mate_left:
                    return False
            ind = right
        return True
            

