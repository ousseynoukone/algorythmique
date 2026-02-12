def palindrome(value):
    normalString = []
    reversedString=[]
    for x in reversed(value):
        normalString.append(x)
    for x  in value:
        reversedString.append(x)

    if("".join(normalString)=="".join(reversedString)):
        return "'{}' est un palindrome".format(value)
    return "'{}' n'est pas un palindrome".format(value)


string = "radar"
result = palindrome(string)

print(result)





