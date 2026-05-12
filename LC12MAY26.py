class Solution:
    def RangeLCMQuery(self, arr, queries):
        def gcd(a,b):
            if a>b:
                a,b=b,a
            if a==0:
                return b
            return gcd(b%a,a)
        def lcm(a,b):
            return a*b//gcd(a,b)
        
        lth=len(arr)
        segtree=[1]*lth+arr
        for ix in range(lth-1,0,-1):
            segtree[ix]=lcm(segtree[ix<<1],segtree[ix<<1|1])
        
        def update(index,value):
            nonlocal lth,segtree
            index+=lth
            segtree[index]=value
            while index>0:
                index>>=1
                segtree[index]=lcm(segtree[index<<1],segtree[index<<1|1])
        
        def query(left,right):
            nonlocal lth,segtree
            left+=lth
            right+=lth+1
            ret=1
            while left<right:
                if left&1:
                    ret=lcm(ret,segtree[left])
                    left+=1
                if right&1:
                    right-=1
                    ret=lcm(ret,segtree[right])
                left>>=1
                right>>=1
            return ret
        
        ret=[]
        for a,b,c in queries:
            if a==1:
                update(b,c)
            elif a==2:
                ret.append(query(b,c))
        return ret


        # code here
