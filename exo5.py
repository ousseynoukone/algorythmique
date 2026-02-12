def sum (number):
    sum = 0
    res = list(map(int, str(number)))

    for x in res :
        sum += int(x)

    return sum



def nestedAddition(number):
    result = number
    if(len(str(result))==1):
        print(result)
        return 


    while(result==number or len(str(result))!=1):
        result = sum(result)
        print(result)



value = 4729

nestedAddition(value)