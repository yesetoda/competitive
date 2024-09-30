class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_loss = set()
        one_loss = set()
        more_loss = set()
        for i in matches:
            if i[0] in more_loss or i[0] in one_loss:
                if i[0] in no_loss:
                    no_loss.remove(i[0])
            else:
                no_loss.add(i[0])  

            if i[1] in no_loss:
                if i[1] in no_loss:
                    no_loss.remove(i[1])
            
                    
            if i[1] in one_loss:
                one_loss.remove(i[1])
                more_loss.add(i[1])
            else:
                if not i[1] in more_loss:
                    one_loss.add(i[1])
        return [sorted(no_loss),sorted(one_loss)]
        