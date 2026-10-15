class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, suffix = [0] * len(nums), [0] * len(nums)
        prefix[0]=1
        suffix[len(suffix) - 1] = 1

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1]*nums[i-1]


        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        
        for i in range(len(nums)):
            nums[i] = suffix[i]*prefix[i]

        return nums
        
            