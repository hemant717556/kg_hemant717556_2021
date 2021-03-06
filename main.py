import sys

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(self.helper(s) == self.helper(t))
        
    def helper(self, s):
        encode = 0
        d = {}
        res = []
        
        for c in s:
            if c not in d:
                d[c] = encode
                encode += 1
            res.append(d[c])
        
        return res
s1=Solution()
x= sys.argv[1]
y=sys.argv[2]

s1.isIsomorphic(x,y)
