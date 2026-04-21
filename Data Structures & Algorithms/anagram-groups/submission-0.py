class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #mapping charCount to list of Anamagrams
                                #also using a defaultdict(list) to create a dict with a empty list
                                #to avoid later transforms
        for s in strs:
            count = [0] * 26 #counting the 26 chars from the alphabet [a, b, c, ... 0, 0, 0]

            for c in s:
                count[ord(c) - ord("a")] +=1 #using the ASCII char value to mapp the char count to the correct alphabet letter
            
            res[tuple(count)].append(s) #appeding the values that match the count of chars 

        print(res)
        return res.values()

        
            


        