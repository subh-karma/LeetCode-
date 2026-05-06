class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        for row in boxGrid:
            empty = n - 1  # position where stone can fall
            for col in range(n - 1, -1, -1): 
                if row[col] == '*':
                    empty = col - 1  # reset empty space on facing obstacle
                elif row[col] == '#':
                    row[col], row[empty] = row[empty], row[col]
                    empty -= 1
        
        # rotate 90 degrees clockwise
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][m - 1 - i] = boxGrid[i][j]
        
        return ans
        
