def replaceByZero(string,n):
    index = []
    cpt = 0
    for i in range (0, len(string)) :
        cpt +=1
        if(cpt==n):
            index.append(i)
            cpt=0

    value = ""
    for i in range (0, len(string)) :
        car = string [i]

        if i in index:
            car = "0"

        value+=car
    return value

        

string = "bonjour"
n = 2

print(replaceByZero(string,n))



