def armstrongNumber(x):
    if x<0:
        return False
    sum=0
    k=len(str(x))
    temp=x
    while(temp!=0):
        rem=temp%10
        sum=sum+pow(rem,k)
        temp=temp//10
      
    return x==sum

print(armstrongNumber(1634))
