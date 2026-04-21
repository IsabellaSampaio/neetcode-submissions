class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        #This solution is the One pass solution and its O(n)
        for i,num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = i
            else:
                return [dic[n], i]
        return 