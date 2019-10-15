# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:05:22 2019

@author: Mohamed
"""
import random
import hangman
import words_hangman


x = random.randint(0, 41)
word = words_hangman.word_list(x)
result = hangman.hangman(word, x)
print(result)
