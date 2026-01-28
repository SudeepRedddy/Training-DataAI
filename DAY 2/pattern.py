# * * * 
# *   *
# * * *
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ",end = " ")
#     print()

# * * * 
#   *
# * * *
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1: 
#             print("*", end=" ")
#         elif i + j  == n- 1 : 
#             print("*", end=" ")
#         else:
#             print(" ",end = " ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1: 
#             print("*", end=" ")
#         elif i == j : 
#             print("*", end=" ")
#         else:
#             print(" ",end = " ")
#     print()


# * 
# * *
# * * *
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# * * * 
# * *
# *
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


 
# 3 
# 3 3 
# 3 3 3
# 4 4 
# 4

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(n,end=" ")
#     print() 
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(n+1,end=" ")
#     print()