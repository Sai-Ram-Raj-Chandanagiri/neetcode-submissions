class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimal one using Dictionaries
        d={}
        min_index = len(nums)+1
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                a=min(i,d[diff])
                b=max(i,d[diff])
                return [a,b]
            else:
                if nums[i] in d:
                    None
                else:
                    d[nums[i]] = i