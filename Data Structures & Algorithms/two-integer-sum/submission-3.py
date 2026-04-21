class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        dic = {}

        #This solution is the One pass solution 
        for i,num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = i
            else:
                arr.append(dic.get(n))
                arr.append(i)
        return arr