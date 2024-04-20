num = int(input("Enter a number"))
counter = 1
result = 1

while(counter<= num):
    result *=counter
    counter += 1
print("factorial of", num, "is" , result)
