class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True) 
        score = 0        
        for i in range(k):
            s = happiness[i] - i 
            score += s if s > -1 else 0            
        return score
        
