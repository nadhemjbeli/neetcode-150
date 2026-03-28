from typing import List
class Solution:
    #Complexity:

    #__encode__
    #Time O(n.m) Where n is the number of strings and m is the averge string length
    #Space O(n.m) Where n.m is the total of characters of the output
    
    #__decode__
    #Time O(n.m) Same reasoning as of encode method
    #Space: O(n.m) the result lists holds all decoded strings

    def encode(self, strs: List[str]) -> str:
        sentence = ''
        for word in strs:
            sentence+=str(len(word))+'@'+word
        return sentence
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i   
            while s[j] != '@':
                j+=1
            res.append(s[j+1:j+1+int(s[i:j])])
            i=j+1+int(s[i:j])
        return res

sol = Solution()
strs = ["hello","worl@d"]
encode = sol.encode(["hello","worl@d"])
decode = sol.decode(encode)
print("result", strs==decode)
