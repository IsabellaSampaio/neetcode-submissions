class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False

        #BRUTE FORCE SOLUTION: O(N^2 log n)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sort = sorted(nums)
                if(sort[i] == sort[j]): 
                    flag = True 
        return flag 


         