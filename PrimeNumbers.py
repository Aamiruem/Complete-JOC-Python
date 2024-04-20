def is_prime(position):  
    if position <= 2:  
        return False  
    for i in range(2, int(position**0.5)+1):  
        if position % i == 0:  
            return False  
    return True  
print(is_prime(2))
