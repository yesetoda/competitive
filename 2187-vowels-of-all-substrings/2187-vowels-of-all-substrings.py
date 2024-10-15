class Solution:
    def countVowels(self, word: str) -> int:
        leng = len(word)
        ans = 0
        vowels = set("aeiou")
        for i in range(leng):
            if word[i] in vowels:
                left = i+1
                right = leng-i
                ans += left*right
        return ans
                