# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:30:26 2024

@author: aamir
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4,5 ,6])

def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in word1:
        if word1.count(i) != word2.count(i):
            return False
    return True

print(anagram("listen","silent"))
