def meanFromMatrix( matrix ):
    n = len(matrix)
    m = len(matrix[0])
    
    array = []
    for i in range(0,n):
        for j in range (0,m):
            array.append(matrix[i][j])
    
    moyen = sum(array)/len(array)
    print("La moyenne est {} ".format(moyen))

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

meanFromMatrix(matrix)

        
