class Solution:
    def findMinDiff(self, arr, M):
        if M == 0 or len(arr) == 0:
            return 0
        n = len(arr)
        if n < M:
            return -1
        arr.sort()
        min_diff = float('inf')
        for i in range(n - M + 1):
            current_diff = arr[i + M - 1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff
