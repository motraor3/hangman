# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:24:42 2019

@author: Mohamed
"""
import words_hangman


def hangman(word, index):
    """A function that plays 'Hangman' with the user. This version chooses
        words from a pre-determined list in the 'words_hangman' module
    :param word: string-type (str) - the word the user is trying to guess
    :param index: integer-type (int) - index of the word obtained from the list
        in the 'words_hangman' module
    :return, answer: string-type - triggered when the user wins, loses or quits
        the game
    """
    wrong = 0
    torso_pieces = 0
    leg_pieces = 0
    stages = ["",
              "______       ",
              "|     |      ",
              "|     0      ",
              "|    /x|x\    ",
              "|    / x\     ",
              "|            "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    guesses = len(stages) - 1
    print("\t\t< Welcome to Hangman!!! >\n")
    print("""<You'll have the chance to guess letters included in the word until
          \ryou reach 6 incorrect guesses.>
          \r<If a letter is present within the word multiple times, then you 
          \rmust correctly guess that letter multiple times. Good luck!>""")
    
    while wrong < guesses:
        print("\n")
        msg = "Guess a letter, or enter 'Quit' to give up ~>  "
        char = input(msg)
        if char == "Quit" or char == 'quit':
            wrong = guesses
        elif char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
            if 1 < wrong <= 4:
                torso_pieces += 1
            elif wrong == 5:
                leg_pieces += 1

        print("\n")
        print("\t" + (" ".join(board)))
        print("~> Current number of incorrect guesses: {}\n".format(wrong))
        first_part = stages[0:4]  
        head = "\n".join(first_part[0:4])   
        torso = stages[4].split("x")
        legs = stages[5].split("x")
        if wrong < 1:
            draw = "\n".join(first_part[0:3])
        else:
            if wrong == 1:
                draw = head               
            elif 1 < wrong <= 4:
                head_torso = first_part + ["".join(torso[0:torso_pieces])]
                draw = "\n".join(head_torso)
            elif wrong == 5:
                full_body = head_torso + ["".join(legs[0:leg_pieces])]
                draw = "\n".join(full_body)
        
        if wrong < guesses:       
            print(draw)
            
        if "_" not in board:
            answer = """\nYou win! The word was: ~ {} ~
            """.format(words_hangman.correct_word(index))
            print("\n" + " ".join(board))
            win = True
            break
        
    if not win:
        stages[4] = stages[4].replace("x", "")
        stages[5] = stages[5].replace("x", "")
        print("\n".join(stages[0:(wrong + 1)]))
        print("\n" + " ".join(board))
        answer = """\n< You lose! The word was ~ {} ~. >
        """.format(words_hangman.correct_word(index))
                                               
    return answer

