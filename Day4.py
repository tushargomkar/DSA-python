# Pattern 1

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def pattern(n):
    for i in range(2*n):
    #   for upper part 
      if i<n:
         for j in range(n-i):
            print("*",end="")
         for j in range(2*i):
             print(" ",end="")
         for j in range(n-i):
             print("*",end="")
        # Lower wala part      
      else:
          for j in range(i-n+1):
              print("*",end="")
          for j in range((2*n-i-1)*2):
              print(" ",end="")
          for j in range(i-n+1):
              print('*',end="")
              
          
      print()
        
        
pattern(5)


# Pattern 2
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

def pattern(n):
    for i in range(2*n-1):
        if i<n:
            for j in range(i+1):
                print("*",end="")
            for j in range((n-i-1)*2):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
        else:
            for j in range(2*n-i-1):
                print("*",end="")
            for j in range((i-n+1)*2):
                print(" ",end="")
            for j in range(2*n-i-1):
                print("*",end="")
        print()
        
pattern(5)





# Pattern 3 
# *****
# *   *
# *   *
# *   *
# *****
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
               print("*",end="")
            else:
               print(" ",end="")
            
        print()
        
pattern(5)
