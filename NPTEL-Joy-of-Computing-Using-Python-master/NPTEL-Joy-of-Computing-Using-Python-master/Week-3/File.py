# import random

# def evolve(x):
    
#     ind = random.randint(0, len(x)-1)
    
#     #if the value of p = 1 then only change the dna from 0 to 1
#     p = random.randint(1, 100)
    
#     if p == 1:
        
#         if(x[ind] == '0'):
            
#             x[ind] = '1'
        
#         else:
            
#             x[ind] = '0'
    


# # with open("dna_data.txt") as myfile:
# with open("file1.txt") as myfile:
    
#     x = myfile.read()
    
#     x = list(x)
    
#     for i in range(0, len(x)):
        
#         evolve(x)
# print(x)









import random

def evolve(x):
    ind = random.randint(0, len(x) - 1)
    
    # If the value of p = 1, then only change the DNA from 0 to 1
    p = random.randint(1, 100)
    
    if p == 1:
        if x[ind] == '0':
            x[ind] = '1'
        else:
            x[ind] = '0'

# Read DNA data from the file
try:
    with open("file1.txt") as myfile:
        x = list(myfile.read())
        
        # Perform mutations
        for i in range(len(x)):
            evolve(x)
        
        # Convert the list back to a string if needed
        x = ''.join(x)
        
        print(x)
except FileNotFoundError:
    print("File not found. Please check the file path.")


# with open("dna_data.txt") as myfile:
with open("Message.txt") as myfile:
    
    x = myfile.read()
    
    x = list(x)
    
    for i in range(0, len(x)):
        
        evolve(x)
print(x)
