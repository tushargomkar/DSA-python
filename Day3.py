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



Pattern 5 



def pattern(n):
    count=1
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
            count=count+1
        print()
        
        
pattern(5)







