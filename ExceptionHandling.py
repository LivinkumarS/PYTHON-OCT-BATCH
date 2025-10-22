a=10

# print(a)
# print(a+10)

# if a<10:
#     print("Hello")

# print(1+"one")

# try:
#     num1=int(input("Enter num1: "))
#     num2=int(input("Enter num2: "))
#     print("The result is: ",num1/num2)
# except ZeroDivisionError:
#     print("Number cannot be divided by 0")
# except ValueError:
#     print("Enter valid input")
# finally:
#     print("Executed Successfully")

# print("Step1")
# print("Step2")


# print(int("hello guys"))

# print("Final Step")

secret_number = 42  

while True:
    try:
        guess = int(input("Guess : "))
        if guess < secret_number:
            print("Too low! ")
        elif guess > secret_number:
            print("Too high! ")
        else:
            print("Correct! ")
            break
    except ValueError:
        print ("Invalid Input!")