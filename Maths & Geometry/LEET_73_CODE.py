def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        var = 1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == 0):
                    if (i == 0):
                        var = 0
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1,m):
            if(matrix[j][0] == 0):
                for i in range(n):
                    matrix[j][i] = 0

        for i in range(1,n):
            if(matrix[0][i] == 0):
                for j in range(m):
                    matrix[j][i] = 0
    
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        
        if var == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        
        
        return matrix