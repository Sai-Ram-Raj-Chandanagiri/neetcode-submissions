class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        new.append(eval("*".join(nums[1:])))
        for i in range(1,len(nums)-1):
            new.append(eval("*".join(nums[:i])+"*"+"*".join(nums[i+1:])))
        new.append(eval("*".join(nums[:len(nums)-1])))
        return new