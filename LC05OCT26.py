class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        res = 0

        for ch in s:
            if ch == '(':
                st.append(res)
                res = 0
            else:
                res = st.pop() + max(res * 2, 1)

        return res
        
