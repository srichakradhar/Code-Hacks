class BinaryMatrix(object):
    def __init__(self, matrix=[]):
        self.matrix = matrix
    def get(self, x, y):
       return self.matrix[x][y]
    def dimensions(self):
       return (len(self.matrix), len(self.matrix[0]))

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        m, n = binaryMatrix.dimensions()
        left_y = n
        for x in range(m):
            left, right = 0, n - 1
            y = (left + right) // 2

            while left <= right:
                if binaryMatrix.get(x, y) == 0:
                    left = y + 1
                else:
                    right = y - 1
                
                y = (left + right) // 2
            
            if left < left_y:
                left_y = left
            
        return -1 if left_y == n else left_y

sol = Solution()
matrix = BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])
print(sol.leftMostColumnWithOne(matrix))