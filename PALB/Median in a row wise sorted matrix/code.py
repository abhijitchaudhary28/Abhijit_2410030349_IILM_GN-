class Solution:
    def median(self, mat):
    	# code here 
        R = len(mat)
        C = len(mat[0])
       
        low = mat[0][0]
        high = mat[0][0]
        
        for i in range(R):
            low = min(low, mat[i][0])
            high = max(high, mat[i][C-1])
            
        desired_count = (R * C + 1) // 2
        
        while low < high:
            mid = low + (high - low) // 2
            total_count = 0
           
            for i in range(R):
                total_count += self.count_le(mat[i], mid)
            
            if total_count < desired_count:
                low = mid + 1
            else:
                high = mid
                
        return low

    def count_le(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            m = l + (r - l) // 2
            if row[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return l
