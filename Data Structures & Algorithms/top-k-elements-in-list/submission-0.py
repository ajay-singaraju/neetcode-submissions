class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        firstDic = defaultdict(int)

        for n in nums:
            firstDic[n] += 1
        
        secondDic = defaultdict(list)
        for n in firstDic:
            secondDic[firstDic[n]].append(n)
        res=[]
        for i in range(len(nums), 0, -1):
            temp = secondDic[i]
            print(secondDic[i])
            for e in temp:
                res.append(e)
                if len(res)==k:
                    return res

        return res