def printAllDivisor(x):
    
    for i in range(1,x+1):
        if x%i==0:
            print(i)
    
    
    
printAllDivisor(12)



# improved version of the code o(n/2)


import math
def printAllDivisor(x):
    
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i==0:
            print(i)
            if((x/i)!=i):
                print(x/i)
    
    
printAllDivisor(36)
