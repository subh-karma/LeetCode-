import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #starting on this number of stones can you win?
        @cache
        def dfs(stones):
            if stones == 0:
                return False # no possible moves

            # check if removing any possible number of stones
            # forces opponent into a losing position
            # if this is the case return true
            for i in range(int(math.sqrt(stones)),0,-1):
               if not dfs(stones - i*i): #opponent cannot win
                return True     

            # if opponent can win from every position we lose
            # return False
            return False

        return dfs(n) # does alice win with n stones?


        
