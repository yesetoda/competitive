class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        d1 = defaultdict(set)        
        for i in freq1:
            d1[freq1[i]].add(i)
        rem = defaultdict(set)
        st = set()
        for i in freq2:
            val = freq2[i]
            if i in d1[val]:
                d1[val].remove(i)
            else:
                rem[val].add(i)
                st.add(i)
        odds = 0
        mp = {}
        sn = set()
        sn2 = set()
        for i in d1:
            if len(d1[i]) == len(rem[i]):
                sn = sn.union(d1[i])
                sn2 = sn2.union(rem[i])
            else:
                return False
        return sn==sn2