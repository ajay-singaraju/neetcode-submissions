class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                num = ord(c) - ord('a')
                count[num] += 1
            
            dic[tuple(count)].append(s)
        
        return list(dic.values())