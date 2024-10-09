# Pattern 1 
# A
# AB
# ABC
# ABCD
# ABCDE

def pattern(n):
    count=1
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end="")
            count=count+1
        print()
        
        
pattern(5)

# Pattern 2 

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 


def pattern(n):
    count=1
    for i in range(n):
        for j in range(i+1):
            print(count,end=" ")
            count=count+1
        print()
        
        
pattern(5)

