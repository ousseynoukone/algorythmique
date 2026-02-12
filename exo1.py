def occurence(array = [], x = 0):
    cpt = 0
    for value in array:
        if(x == value):
            cpt+=1
    return cpt


tableau = [4, 2, 4, 7, 4, 9]
x = 4
cpt = occurence(tableau,x)

print(" {} est present {} fois".format(x, cpt))