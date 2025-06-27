class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSubSeq(s,t):
            i = j = 0
            m = len(s)
            n = len(t)

            while i < m and j < n:
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == n
        n = len(s)
        count = Counter(s)
        allowedCount = defaultdict(int)

        for c , cnt in count.items():
            if cnt >= k:
                allowedCount[c] = cnt//k
        sortedLetters = sorted(allowedCount.keys() , reverse=True)

        cand = []
        for c in sortedLetters:
            cnt = defaultdict(int)
            cnt[c] += 1
            cand.append((c,cnt))
        while True:
            newCand = []
            for cur , cnt in cand:
                for c in sortedLetters:
                    allowedCnt = allowedCount[c]
                    if cnt[c] < allowedCnt:
                        if isSubSeq(s, (cur+c)*k):
                            newCnt = cnt.copy()
                            newCnt[c] += 1
                            newCand.append((cur+c, newCnt))
            if not newCand:
                break
            cand = newCand
        return cand[0][0] if cand else ""
        
        
