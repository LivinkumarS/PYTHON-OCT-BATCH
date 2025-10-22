class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # methods
    def isPresent(self):
        print("Yes Present!")
    def canVote(self):
        if(self.age>17):
            print("Yes")
        else:
            print("No")
            
class Pen(Student):
    def __init__(self,color):
        self.color=color
    
    # methods
    def write(self):
        print("Writing")
            
# Student --> 2 attrributes 2- methods
a='10'
stu1=Student("saravanan",23)
pen1=Pen('Black')


# stu1.isPresent()
# stu1.canVote()
# pen1.write()

print(type(pen1))

# b="hello" #class str
b=[1,2,3,4,"hello"] #class list
