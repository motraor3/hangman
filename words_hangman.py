# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:14:44 2019

@author: Mohamed
"""

def word_list(x):
    """
    This function contains a list of words that the computer chooses from in
    order to initiate the game 'hangman' contained in module 'hangmanCh10STP.py'
    :param x: integer-type, a random integer from 'hangmanCh10STP.py' used to
        select a word for the 'hangman'-function
    :return, choice: string-type, the word the computer supplies to the user
        to guess in the 'hangman'-function within the 'hangmanCh10STP.py' module
    """

    words = ["cat", "hat", "rat", "self", "programmer", "human", "tattoo",
             "treasure", "happy", "demoralized", "loop", "template", "hangman",
             "variable", "parameter", "definition", "function", "python",
             "coding", "float", "integer", "string", "list", "dictionary",
             "key", "file", "hawkeye", "iowa", "lonely", "single", "taken",
             "depressed", "anxiety", "lost", "attachment", "confused", "copy",
             "regret", "misfortune", "past", "mistakes", "regrets"]
    
    choice = words[x]
    
    return choice


def correct_word(x):
    
    words = ["cat", "hat", "rat", "self", "programmer", "human", "tattoo",
             "treasure", "happy", "demoralized", "loop", "template", "hangman",
             "variable", "parameter", "definition", "function", "python",
             "coding", "float", "integer", "string", "list", "dictionary",
             "key", "file", "hawkeye", "iowa", "lonely", "single", "taken",
             "depressed", "anxiety", "lost", "attachment", "confused", "copy",
             "regret", "misfortune", "past", "mistakes", "regrets"]
    answer = words[x]
    
    return answer
    
