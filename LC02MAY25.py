class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        cur = deque()

        # Find all indices of dominoes that might affect others
        for i in range(len(dominoes)): 
            if dominoes[i] == 'L' and i>0 and dominoes[i-1] == ".":
                cur.append(i) 
            if dominoes[i] == 'R' and i < len(dominoes)-1 and dominoes[i+1] == '.': 
                cur.append(i)
        
        while cur: 
            nxt = set()  # Set to be added to the next iteration
            for k in range(len(cur)):   # Process entire queue at once
                i = cur.popleft() 

                if dominoes[i] == 'L' and i>0:
                    if dominoes[i-1] == ".": 
                        # Can fall
                        dominoes[i-1] = 'L'
                        nxt.add(i-1)
                    elif dominoes[i-1] == 'R' and (i-1) in nxt:     
                        # Balances out, and remove it from the set
                        dominoes[i-1] = '.'
                        nxt.remove(i-1)

                if dominoes[i] == 'R' and i < len(dominoes)-1 :
                    if dominoes[i+1] == ".":
                        dominoes[i+1] = 'R'
                        nxt.add(i+1)
                    elif dominoes[i+1] == 'L' and (i+1) in nxt: 
                        dominoes[i+1] = '.'
                        nxt.remove(i+1)
            
            cur += list(nxt)
                
        return ''.join(dominoes)
