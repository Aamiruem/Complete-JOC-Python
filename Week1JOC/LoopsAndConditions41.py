# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:15:26 2024

@author: aamir
"""

for i in range(1, 51):
    if(i%3 == 0):
      print(str(i) + " = Fizz")
    else:
        if(i%5 == 0):
          print(str(i) + " = Buzz")
        else:
          if(i%3 == 0 and i%5 == 0):  
              print(str(i) + " = FizzBuzz")
          else:
              print(str(i))
              
              
              
def fizzBuzz(r):
    for i in range(1, r):
        if(i%3 == 0 and i%5 == 0):
            print(str(i) + " = fizzBuzz")
        else:
            if(i%3 == 0):
                print(str(i) + " = fizz")
            else:
                if(i%5 ==0):
                    print(str(i) + " = Buzz")
                else:
                    print(str(i))
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    