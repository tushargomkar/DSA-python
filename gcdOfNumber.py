#Time complicety O(N)

def GCD(x1,x2):
    gcd=0
    for i in range(1,min(x1,x2)+1):
        if x1%i==0 and x2%i==0:
            gcd=i
    return gcd
    
print(GCD(12,24))


# Better than the approch but the worse 
# case min of x1 and x2
def gcdNumber(x1,x2):
    gcd=0
    for i in range(min(x1,x2),0,-1):
        # print(i)
        if x1%i==0 and x2%i==0:
            gcd=i
            break
    return gcd

print(gcdNumber(12,24))


