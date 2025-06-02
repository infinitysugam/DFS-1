# Time Complexity = O(m*n)
# Space Complexity = O(m*n)

from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):

        row = len(image)
        col = len(image[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]


        original_pixel = image[sr][sc]

        if original_pixel == color:
            return image

        queue = deque()
        queue.append([sr,sc])
        image[sr][sc]=color

        while queue:
            r,c = queue.popleft()
            for i,j in dirs:
                if r+i>=0 and r+i<row and c+j>=0 and c+j<col and image[r+i][c+j]==original_pixel:
                    image[r+i][c+j]=color
                    queue.append([r+i,c+j])


        return image 




        
        