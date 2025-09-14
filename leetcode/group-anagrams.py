class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for i in strs:
            temp = list(i)
            temp.sort()
            if "".join(temp) not in keys:
                keys["".join(temp)] = [i]

            else:
                keys["".join(temp)].append(i)

        lst = []

        for i in keys:
            lst.append(keys[i])

        return lst

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         final = []
#         for i in range(len(strs)):
#             new = strs[:i] + strs[i + 1:]
#             curr = [strs[i]]
#             for j in new:
#                 if self.isAna(strs[i], j):
#                     curr.append(j)
#             curr.sort()

#             if curr not in final:
#                 final.append(curr)

#         return final

#     def isAna(self, a: str, b:str) -> bool:
        
#         if len(a) != len(b):
#             return False
        
#         map1 = {}
#         map2 = {}

#         for i in a:
#             if i in map1:
#                 map1[i] += 1
#             else:
#                 map1[i] = 1

#         for i in b:
#             if i in map2:
#                 map2[i] += 1
#             else:
#                 map2[i] = 1

#         return map1 == map2