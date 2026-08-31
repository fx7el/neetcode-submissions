class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''l=[]
        a=0
        while a<len(nums):
            j=a
            k=1
            for i in range(len(nums)):
                if i!=j:
                    k*=nums[i]
            l.append(k)
            a+=1
        return l'''

        res=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        pos=1
        for i in range(-1,-len(nums)-1,-1):
            res[i]*=pos
            pos*=nums[i]
        return res