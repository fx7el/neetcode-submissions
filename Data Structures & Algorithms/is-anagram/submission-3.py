class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t) 
        #(or)
        #return Counter(s)==Counter(t)  
        if len(s)!=len(t):
            return False
        a,b={},{}
        for i in range(len(s)):
            a[s[i]]=a.get(s[i],0)+1
            b[t[i]]=b.get(t[i],0)+1
        for j in a:
            if a[j]!=b.get(j,0):
                return False
        return True   