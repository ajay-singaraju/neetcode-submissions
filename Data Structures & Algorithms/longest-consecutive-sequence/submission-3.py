class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        max_length = 0
        current_num = 0
        current_length = 0

        for num in hashset:
            if num - 1 not in hashset:
                current_length = 1
                current_num = num
            
            while current_num + 1 in hashset:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)

        return max_length


