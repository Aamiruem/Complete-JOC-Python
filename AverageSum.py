num = []
n = int(input("Enter the number of elements"))
for i in range(n):
    item = int(input("Enter the item" + str(i+1) + ": "))
    num.append(item)
    result = sum(num)
    average = result/n
print("The average is", average)
