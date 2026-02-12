
from itertools import zip_longest

def buildMatrice( a ,  b):
    if(type(a)!= int or type(b)!= int):
        print("Verifiez que les valeurs sont bien des entiers")
        return
    
    if(a<=0 or b <=0):
        print("Que des valeurs positives sont authorised")
        return
    matrix = []

    for i in range(0,a):
        array = []
        for i in range(0,b):
            array.append(0)

        matrix.append(array)
    
    return matrix

n = 3
m = 4

result = buildMatrice(n,m)

print(result)

    



      
    

