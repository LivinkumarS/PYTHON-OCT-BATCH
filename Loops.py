# a=0

# while a<5: 
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print()
#     print("---------------------")
#     print()
#     a-=1
    
# a --> 0,-1,-2,-100......
# cond ---> True
# no of execution---> 1,2,3,4,5

# str1="Hello world"
# print(str1[10])

# str1="123456789"
# print(len(str1))

# for i in range(100):
#     print(i)
# for i in range(3,10,3):
#     print(i)

# 1-- k
# 2-- a
# 3-- n
# 4-- t

# 0,1,2,3,4,5,6,7,8,9

# for i in range(10):
#     if i==7:
#         continue
#     print(i)
    
# i=0

# while i<10:
#     if i==7:
#         i+=1
#         continue
#     print(i)
#     i+=1

#i=0,1,2,3,4,5,6,7
#no of executions: 1,2,3,4,5,6,7

#1 to 100

# for i in range(1,101):
#     print(i)

# Number guess

secret_number=33

while True:
    inp=int(input("Enter a number: "))
    if inp==secret_number:
        print("You won!")
        break
    else:
        print("Try again!")
    
# until he finds the correct number