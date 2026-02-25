a = input("Enter a string: ")

a = a.lower()  

b = a[::-1]

print("Reversed string is:", b)

if a == b:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")