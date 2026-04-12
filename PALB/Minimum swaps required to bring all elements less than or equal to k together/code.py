class Solution:
        
    def minSwap (self,arr, k) : 
        #Complete the function
        n = len(arr)
        fav = 0
        for x in arr:
            if x <= k:
                fav += 1
        if fav <= 1:
            return 0
        bad = 0
        for i in range(fav):
            if arr[i] > k:
                bad += 1
        ans = bad
        for i in range(0, n - fav):
            if arr[i] > k:
                bad -= 1
            if arr[i + fav] > k:
                bad += 1
            ans = min(ans, bad)
            
        return ans
