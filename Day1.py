

# Pattern 1
# *****
# *****
# *****
# *****
# *****
def _pattern_(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
_pattern_(5)




# Pattern 2
# *
# **
# ***
# ****
# *****

def _pattern_(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end="")
        print()
_pattern_(5)


# Pattern 3
# 1
# 12
# 123
# 1234
# 12345

def _pattern_(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1,end="")
        print()
_pattern_(5)




# Pattern 5



# 1
# 22
# 333
# 4444
# 55555

def _pattern_(n):
    for i in range(n+1):
        for j in range(i):
            print(i,end="")
        print()
_pattern_(5)


# Pattern 5
# *****
# ****
# ***
# **
# *

def _pattern_(n):
    for i in range(n+1):
        for j in range(n-i):
            print("*",end="")
        print()
_pattern_(5)




# Pattern 6
# 12345
# 1234
# 123
# 12
# 1
def _pattern_(n):
    for i in range(n+1):
        for j in range(n-i):
            print(j+1,end="")
        print()
_pattern_(5)


