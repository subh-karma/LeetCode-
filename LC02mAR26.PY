class Solution:
    def minSwaps(self, g: List[List[int]]) -> int:
        res,g = 0,[len(r)-len([*takewhile(not_,r[::-1])]) for r in g]
        for i in range(len(g)):
            for ii,q in enumerate(g):
                if q<=i+1: res += ii; g.pop(ii); break
            else: return -1

        return res
        
