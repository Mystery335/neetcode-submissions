class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lst = defaultdict(list)
        for string in strs:
            strCount = [0] * 26
            for x in range(len(string)):
                strCount[ord(string[x]) - ord('a')] += 1
            lst[tuple(strCount)].append(string)

        return list(lst.values())