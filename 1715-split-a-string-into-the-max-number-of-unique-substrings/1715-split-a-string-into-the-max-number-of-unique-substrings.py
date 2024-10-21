class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        _max= 0
        leng = len(s)
        def sub_str(index,path):
            nonlocal _max
            nonlocal leng
            if index ==leng:
                _max = max(_max,len(path))
            for i in range(index,leng):
                val = s[index:i+1]
                if not val in path:
                    path.add(val)
                    sub_str(i+1,path)
                    path.remove(val)
        sub_str(0,set())
        return _max