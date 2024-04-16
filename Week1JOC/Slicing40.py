# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:38:52 2024

@author: aamir
"""

student = ["Aamir", "kamran", "Afroz", "Shahbaj", "Jawed", "Gulrej"]

print(student)
['Aamir', 'kamran', 'Afroz', 'Shahbaj', 'Jawed', 'Gulrej']

student[:]
 
             



student[:]

student.sort()

print(student)
['Aamir', 'Afroz', 'Gulrej', 'Jawed', 'Shahbaj', 'kamran']

student[3:]

student[3:2]


student[3:4]


student[:5]

student[:6]

student[0:6]

student[4:6]







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
       







