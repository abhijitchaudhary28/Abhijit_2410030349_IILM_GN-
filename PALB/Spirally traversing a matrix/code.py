class Solution:
    def spirallyTraverse(self, mat):
       # code here
        if not mat or not mat[0]:
            return []
        rows = len(mat)
        cols = len(mat[0])
        
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        
        result = []
        
        while top <= bottom and left <= right:
           
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
                
        return result
            
