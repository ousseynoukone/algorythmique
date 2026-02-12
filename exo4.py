def sum (number):
    sum = 0
    res = list(map(int, str(number)))

    for x in res :
        sum += int(x)

    return sum
    
valeur = 4729
result = sum(4729)

print("La somme de {} est {} ".format(valeur,result))