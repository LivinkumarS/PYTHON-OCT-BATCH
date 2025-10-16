# str1[0]=2
# print(str1[2:])
# print(str1[:4])
# print(str1[2:7])
# print(str1[::-1])

# print(str1*4)

# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
# print(str1.title())

# print(str1)
# print(str1.strip())

# str1="Hello world"

# print(str1.replace("Hello","Hi"))

# lis=str1.split(" ")

# print(lis)

# lis1=['Hello', 'world', "Hi","world","!"]

# ans='--'.join(lis1)
# print(ans)

# print(str1.count('hell'))
# print(str1.find('s'))

# print(str1.startswith("ell"))
# print(str1.endswith("ld"))

# print("man" in "woman")
# print("man" not in "woman")

str=input("Enter a string: ")
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")