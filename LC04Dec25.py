class Solution:
    def countCollisions(self, s: str) -> int:
        return len(s.lstrip('L').rstrip('R').replace('S',''))
        
