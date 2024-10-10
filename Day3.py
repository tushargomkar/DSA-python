# Pattenrn 3 

# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

def pattern(n):
    count=1
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end=" ")
            count=count+1
        print()
        
        
pattern(5)

# Pattern 4 

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 


def pattern(n):
    count=1
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
            count=count+1
        print()
        
        
pattern(5)


# Pattern 6 
#       A 
#     A B A 
#   A B C B A 
# A B C D C B A 
def pattern(n):
    
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
            # Left Tringle 
        for j in range(i):
            print(chr(65+j),end=" ")
            # Right triangle 
        for j in range(i,-1,-1):
            print(chr(65+j),end=" ")
        print()
        
        
pattern(4)



# Pattern 7
# E
# DE
# CDE
# BCDE
# ABCDE
def pattern(n):
    k=n-1
    for i in range(n):
        for j in range(i+1):
            print(chr(65+k+j),end="")
        k=k-1
        print()
        
        
pattern(5)













