class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        chart = {}
        count = 0

        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] +=1
        
        for char in t:
            if char not in chart:
                chart[char] = 1
            else:
                chart[char] +=1
        
        if(chart == chars):
            return True
        return False


                
        