# # The manual way of linklist 
# print(int(-3/2))
# print(3//1)

# for i in range(1,6):
#     print(i) 

for i in range(10,1,-1):
    print(i)   

nums=[1,2,3,4,5]


for i,n in enumerate(nums):
    print(i,n)

nums1=['tuple','list','dict',"a"]

arr = [[i*3+j+1 for j in range(3)] for i in range(3)]
print(arr)
