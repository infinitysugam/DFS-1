# Time Complexity = O(m*n)
# Space Complexity = O(m*N)
from collections import deque
class Solution:
    def updateMatrix(self, mat):

        row = len(mat)
        col = len(mat[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        boolean_matrix = [[-1 for i in range(0,col)] for j in range(0,row)]
        print(boolean_matrix)
        queue = deque()

        for i in range(0,row):
            for j in range(0,col):
                if mat[i][j]==0:
                    boolean_matrix[i][j]=0
                    queue.append([i,j])
        
        level = 0 

        while queue:
            size = len(queue)
            for i in range(0,size):
                r,c = queue.popleft()

                for x,y in dirs:
                    if r+x>=0 and r+x<row and c+y>=0 and c+y<col and mat[r+x][c+y]==1 and boolean_matrix[r+x][c+y]==-1:
                        boolean_matrix[r+x][c+y]=level+1
                        queue.append([r+x,c+y])

            
            level = level + 1
        
        return boolean_matrix
