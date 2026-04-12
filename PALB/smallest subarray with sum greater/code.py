class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        current_sum = 0
        min_len = n + 1
        start = 0
        end = 0
        
        while end < n:
            current_sum += arr[end]
            while current_sum > x:
                min_len = min(min_len, end - start + 1)
                current_sum -= arr[start]
                start += 1  
            end += 1
        return min_len if min_len <= n else 0
        
