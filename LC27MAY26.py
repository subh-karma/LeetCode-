class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()


        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)

        c = 0

        for ch in lower:
            ind=word.rfind(ch)
            if ch.upper() in upper:
                if ind<word.index(ch.upper()):
                    c += 1

        return c
        
