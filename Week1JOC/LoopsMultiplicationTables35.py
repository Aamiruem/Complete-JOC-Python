# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:19:39 2024

@author: aamir
"""

n = input("What tables would you like to display? ")
n = int(n)
for i in range(11):
    print(n, "X", i, "=", n*i)
