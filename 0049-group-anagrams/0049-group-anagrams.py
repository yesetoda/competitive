class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        str1 = list(map(lambda x:"".join(sorted(x)),strs))
        # print(str1)
        for i in range(len(strs)):
            freq[str1[i]].append(strs[i])
        return list(freq.values())