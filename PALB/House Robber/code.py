class Solution(object):
    def rob(self, nums):
        
        if not nums:
            return 0
        prev_max = 0
        curr_max = 0
        
        for x in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + x)
            prev_max = temp
            
        return curr_max
