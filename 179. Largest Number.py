from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert integers to strings
        nums = list(map(str, nums))
        
        # Custom sorting function
        def compare(x, y):
            return 1 if x + y < y + x else -1  # Sort in descending order
        
        # Sort numbers based on our custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join sorted numbers
        result = "".join(nums)
        
        # Remove leading zeros (case: [0,0])
        return "0" if result[0] == "0" else result
