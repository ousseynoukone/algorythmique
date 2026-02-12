def canBeTriangle(a,b,c):

    if (a + b <= c or a + c <= b or b + c <= a):
        print("Pas un triangle mon reuf")
        return False
    
    if((a*a) + (b*b) == (c*c)):
        print("Rectangle")
        return True

    if(a==b and b==c):                 
        print("équilatéral")
        return True
    

        
    



a = 1
b = 2
c = 3

canBeTriangle(a,b,c)