# list1= [1,2,3,"four","five","six",True,False,3,2,1]
# True==1

# list1[6]=False
# list1.append("hello")
# list1.append("world")

# list1.insert(0,"hello")

# list1.remove(3)
# list1.pop()
# list1.pop(3)

# list1.remove(True)
# list1.remove(True)
# list1.remove(True)

# print(list1)

# if 0:
#     print("Hi")

# lis2=[34,2,34,56,34,32,45,67,78,7,42,314,24,46]
# lis2.sort()
# lis2.reverse()
# print(lis2)


# Tuple 


# tup1=(2,1,3,"hello","hi",2,1,3)

# tup1[5]=5

# print(tup1)

# person1=("ken",33)

# # name=person1[0]
# # age=person1[1]

# name,age=person1

# print(name,age)


# Set

# set1={1,2,3,4,5,6,7,8}
# set2={7,8,9,10,11,12}

# # print(set1.union(set2))
# # print(set1.intersection(set2))
# print(set2.difference(set1))

# Dictionary

# dict1={
#     1:"one",
#     2:"two",
#     3:"three",
# }

# dict1[2]="twenty two"

# print(dict1)

# person1={
#     "name":"Vijay",
#     "age":52,
#     "isMarried":True
# }

# print(person1["age"])

# print(person1.keys())
# print(list(person1.values()))
# print(list(person1.items()))

lis=[
    1,
    2,
    3,
    4,
    [
        "five",
        "six",
        "seven",
        [
            "eight",
            "nine",
            "ten"
        ]
    ]
]

print(lis[-1][-1][-1][-1])