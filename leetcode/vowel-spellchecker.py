class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        exact = set(wordlist)

        capsCases = {}
        vowelsCases = {}

        for i in wordlist:
            lower = i.lower()
            if lower not in capsCases:
                capsCases[lower] = i

        for i in wordlist:
            safe = self.hideVowels(i)
            if safe not in vowelsCases:
                vowelsCases[safe] = i

        ans = []
        for i in queries:
            if i in exact:
                ans.append(i)
            elif i.lower() in capsCases:
                ans.append(capsCases[i.lower()])
            elif self.hideVowels(i) in vowelsCases:
                ans.append(vowelsCases[self.hideVowels(i)])
            else:
                ans.append("")

        return ans


    def hideVowels(self, s: str) -> str:
        for i in range(len(s)):
            s = s.lower()
            if s[i] in "aeiou":
                s = s[:i] + "*" + s[i + 1:]
        
        return s



# class Solution:
#     def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

#         output = []

#         setlst = set(wordlist)

#         print(setlst)

#         for i in queries:

#             li = i.lower()

#             if i in setlst:
#                 output.append(i)
#                 continue
            
#             else:
#                 found = False

#                 for j in wordlist:
#                     lj = j.lower()
#                     if li == lj:
#                         output.append(j)
#                         found = True
#                         break
                
#                 if not found:
#                     for j in wordlist:
#                         if self.vowelcheck(li, j.lower()):
#                             output.append(j)
#                             found = True
#                             break

#                 if not found:
#                     output.append("")

#         return output

#     def vowelcheck(self, a: str, b: str) -> bool:

#         if len(a) != len(b):
#             return False

#         vowels = "aeiou"

#         for i in range(len(a)):

#             if a[i] not in vowels and b[i] not in vowels and a[i] != b[i]:
#                 return False

#             elif (a[i] in vowels and b[i] not in vowels) or (a[i] not in vowels and b[i] in vowels):
#                 return False

#         return True