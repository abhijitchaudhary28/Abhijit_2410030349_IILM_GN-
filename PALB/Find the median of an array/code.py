class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
        if n % 2 != 0:
            return arr[n // 2]
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (arr[mid1] + arr[mid2]) // 2
