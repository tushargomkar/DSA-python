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
