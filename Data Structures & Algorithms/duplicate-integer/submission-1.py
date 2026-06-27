class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #bruteforce
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # else:
        #     return False
        
        #Using Hashmap
        dictionary = {}
        for i in nums:
            if i in dictionary.keys():
                return True
            else:
                dictionary[i] = 1
        else:
            return False