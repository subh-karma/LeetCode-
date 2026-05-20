class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        curr = 0 # counter of common elements

        C = [0] * n # result

        # hashtables
        a = [0] * (n + 1)
        b = [0] * (n + 1)

        # iterating both arrays
        for i in range(n):

            # trying to match A[i]
            if b[A[i]] > 0:
                # match found! Adjust the frequency
                b[A[i]] -= 1
                curr += 1
            else:
                a[A[i]] += 1
            
            # trying to match B[i]
            if a[B[i]] > 0:
                # match found! Adjust the frequency
                a[B[i]] -= 1
                curr += 1
            else:
                b[B[i]] += 1

            # set result for current index
            C[i] = curr

        # end :)
        return C
        
