class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ncol=len(matrix[0])
        nrow=len(matrix)
        rowzero=False

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:rowzero=True
        for i in range(1,nrow):
            for j in range(1,ncol):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(1,nrow):
                matrix[i][0]=0
        if rowzero:
            for i in range(ncol):
                matrix[0][i]=0
