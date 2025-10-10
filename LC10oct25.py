class Solution:
    def zigZagTraversal(self, root):
        ret=[]
        lvl=0
        q=[root]
        while q:
            tmp=[]
            nq=[]
            for cur in q:
                if cur==None:
                    continue
                tmp.append(cur.data)
                nq.extend([cur.left,cur.right])
            lvl+=1
            if lvl%2==1:
                ret.extend(tmp)
            else:
                ret.extend(tmp[::-1])
            q=nq
        return ret
