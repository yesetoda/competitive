class Solution:
    def passThePillow(self, n: int, time: int) -> int:
            return n - ( time % ( n - 1 ) ) % n if ( time // ( n - 1 ) ) % 2 else ( time % ( n - 1 ) ) + 1