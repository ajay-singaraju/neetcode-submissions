class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        maxcount = 0
        maxn = 0

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

            if counts[n] > maxcount:
                maxcount = counts[n]
                maxn = n
            
        return maxn
        