class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        
        return k
