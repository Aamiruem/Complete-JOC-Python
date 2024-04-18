import random
year = random.randint(1993, 2024)
print(year)
if(year %4 ==0 and year %100 !=0 or year %400 ==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")





import random
n = input("Enter the number of years : ")
n = int(n)

for i in range(n):
    print(random.randint(1993, 2024))
    
year = random.randint(1993, 2024)
print(year)
if(year %4 ==0 and year %100 !=0 or year %400 ==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
