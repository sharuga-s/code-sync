class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        map = {}

        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = 0
            map[s[i]] += 1

        print(map)
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i

        return -1