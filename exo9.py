def replaceInMatrix(matrix,i,j,n):
    if(type(i)!= int or type(j)!= int or type(n)!= int):
        print("Verifiez que les valeurs sont bien des entiers")
        return
    
    if(i<0 or j <0 or n <0):
        print("Seuls les valeurs positifs ou nul sont authorised !")
        return
    
    matrix[i][j] = n

    return matrix

matrix = [
[1, 2],
[3, 4],
[5, 6]
]
i = 1
j = 0
n = 10


result = replaceInMatrix(matrix,i,j,n)

print(result)