class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix);
        m=len(matrix[0]);
        for i in range(0,n-1):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j];
        
        for i in range(0,n):
            start=0;
            end=m-1;
            while start < end:
                matrix[i][start],matrix[i][end] = matrix[i][end],matrix[i][start];
                start+=1;
                end-=1;
        
