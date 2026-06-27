class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #BruteForce
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        #Optimal Approach: 
        d={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d.keys():
                return sorted([i,d[diff]])
            else:
                d[nums[i]]=i
