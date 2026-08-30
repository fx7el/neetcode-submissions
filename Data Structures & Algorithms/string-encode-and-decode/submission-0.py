class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        res,j=[],0
        while j<len(s):
            i=j
            while s[i]!="#":
                i+=1
            length=int(s[j:i])    
            res.append(s[i+1:i+1+length])
            j=i+1+length
        return res