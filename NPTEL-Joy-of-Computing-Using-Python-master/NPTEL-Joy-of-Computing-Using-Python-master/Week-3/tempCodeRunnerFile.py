import random

def evolve(x):
    
    ind = random.randint(0, len(x)-1)
    
    #if the value of p = 1 then only change the dna from 0 to 1
    p = random.randint(1, 100)
    
    if p == 1:
        
        if(x[ind] == '0'):
            
            x[ind] = '1'
        
        else:
            
            x[ind] = '0'
    