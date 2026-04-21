class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        #Better solution, using hashmap: O(n)

        '''
        Iterate Through the List: 
            For each element in the list:
                Check if the element already exists in the hash map.
                If it exists, you have found a duplicate.
                If it doesn't exist, add it to the hash map.'''

        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate[num] = num
        return False
            

         