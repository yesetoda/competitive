class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev = skill[0]+skill[-1]
        chemistry = 0
        leng =len(skill)
        for i in range(leng//2):
            val = skill[i]+skill[leng-i-1]
            print(skill[i],skill[leng-i-1])
            if prev != val:
                return -1
            else:
                chemistry+= skill[i]*skill[leng-i-1]
        return chemistry

                

        