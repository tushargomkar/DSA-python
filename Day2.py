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



# Pattern 4







