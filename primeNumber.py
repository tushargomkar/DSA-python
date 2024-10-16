#Brutu force Method O(N)

def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    print(count)
    if count>2:
        return False
    else:
        return True
print(prime(97))







#optimise metheod O(sqrt(n))


import math
def findPrimeNumber(x):
    count=0
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i==0:
            count+=1
            if((x/i)!=i):
                count+=1
              
    if count>2:
        return False
    else:
        return True
    
print(findPrimeNumber(5))
