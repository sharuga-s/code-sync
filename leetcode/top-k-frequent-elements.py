class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}

        output = []

        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        for i in range(k):
            max = 0
            curr = 0

            for j in map:
                if map[j] > max:
                    max = map[j]
                    curr = j

            map.pop(curr)
            output.append(curr)

        return output