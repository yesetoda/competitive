class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        leng = len(arr)
        q = deque([start])
        seen = set()
        while q:
            ln = len(q)
            for _ in range(ln):
                cur = q.popleft()
                seen.add(cur)
                if arr[cur] == 0:
                    return True
                if cur+arr[cur]<leng and not cur+arr[cur] in seen:
                    if arr[cur+arr[cur]] == 0:
                        return True
                    q.append(cur+arr[cur])
                    seen.add(cur+arr[cur])
                if cur-arr[cur]>=0 and not cur-arr[cur] in seen:
                    if arr[cur-arr[cur]] == 0:
                        return True
                    q.append(cur-arr[cur])
                    seen.add(cur-arr[cur])
            
        return False

                