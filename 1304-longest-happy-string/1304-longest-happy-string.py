class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        if a>0:
            hp.append([-a,"a"])
        if b>0:
            hp.append([-b,"b"])
        if c>0:
            hp.append([-c,"c"])
        
        heapify(hp)
        ans = []
        while hp:
            freq,chr = heappop(hp)
            freq *= -1
            cnt = min(2,freq)
            ans.append(chr*cnt)
            freq-=cnt
            if hp:
                if -hp[0][0] <= freq :
                    nxt,ch = heappop(hp)
                    nxt *= -1
                    ans.append(ch)
                    nxt-=1
                    if nxt>0:
                        heappush(hp,[-nxt,ch])
                if freq>0:
                    heappush(hp,[-freq,chr])
            else:
                break
            # print(ans)
        return ''.join(ans)


            