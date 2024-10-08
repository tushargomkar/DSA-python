# Pattern 1
#     *
#   ***
#   *****
#  *******
# *********

def _pattern_(n):
    for i in range(n):
        # 1 for is for the space 
        for j in range(n-1-i):
            print(" ",end="")
        # 2 for the * logic    
        for j in range(2*i+1):
            print("*",end="")
        print()
    
        
_pattern_(5)



# Pattern 2

# *********
#  *******
#   *****
#    ***
#     *
def _pattern_(n):
    for i in range(n):
        # 1 for is for the space 
        for j in range(i):
            print(" ",end="")
        # 2 for the half down tringle    
        for j in range(n-i-1):
            print("*",end="")
        #  3 for the rest down tringle
        for j in range(n-i):
            print("*",end="")
        print()
    
        
_pattern_(5)


# Pattern 3
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
    
def _pattern_(n):
    for i in range(n):
        # 1 for is for the space 
        for j in range(n-1-i):
            print(" ",end="")
        # 2 for the * logic    
        for j in range(2*i+1):
            print("*",end="")
        print()
    
        
_pattern_(5)   

def _pattern_(n):
    for i in range(n):
        # 1 for is for the space 
        for j in range(i):
            print(" ",end="")
        # 2 for the half down tringle    
        for j in range(n-i-1):
            print("*",end="")
        #  3 for the rest down tringle
        for j in range(n-i):
            print("*",end="")
        print()
    
        
_pattern_(5)


# Second Approach for the * pattern 
def pattern(n):
   for i in range(2 * n):
    if i < n:
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end=" ")
    else:
        for j in range(i - n + 1):
            print(" ", end="")
        for j in range(2 * n - i - 1):
            print("*", end=" ")
    print()
    
    
    
pattern(5)


# Pattern 4

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        print()

pattern(5)


# Alternate Approach
def pattern(n):
    for i in range(2*n-1):
        if i<n:
            for j in range(i+1):
                print("*",end="")
        else:
            for j in range(2*n-i-1):
                print("*",end="")
        print()

pattern(5)



# Pattern 6

# 1
# 01
# 101
# 0101
# 10101

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print("1",end="")
            else:
                print("0",end="")
        print()
        
        
pattern(5)


# Pattern 6 
# 1      1
# 12    21
# 123  321
# 12344321

def pattern(n):
    for i in range(n):
        # for the first tringle pattern 
        for j in range(i+1):
            print(j+1,end="")
            
        # for the space pattern 
        for j in range((n-i-1)*2):
            print(" ",end="")
      
        
        # for the pattern in the last after the array
        for j in range(i+1,0,-1):
            print(j,end="")
        print()
        
pattern(4)












