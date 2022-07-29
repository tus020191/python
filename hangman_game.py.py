from random import choice
from collections import Counter
from threading import Event,Thread,Timer
from time import  sleep
"""
        **************************** hangman game ******************************************************* 
"""

class hangman:
    def __init__(self):
        self.fruits="apple banana mango lemon lychee muskmelon papaye pineapple berry peach " \
                    "watermelon coconut strawberry"

        self.lst=self.fruits.split(" ")
        self.word=choice(self.lst)

        self.chances=len(self.word)+2
        self.guess=""
        self.letter_guess="" # store the so far gussed character
        self.count=0
        self.ans=0
        self.t=0
        self.flag=0
    def timer(self):

        print("time out  for this chance  press enter !!!! ")
        self.chances-=1
        self.t=0


    def start_game(self):
        if(self.flag!=1):
            print("Guess the word !!! It is a name of fruit from the following list :\n {}".format(self.lst))
            print()
            print("you are given {} chances".format(self.chances))
            print("per chance you will have 10 seconds.......")
            print("\t\t\t\t",end="")
            for i in self.word:
                print("{:>7}".format("_"),end="")
            print()
            self.flag=1
        try:
            while(self.chances>0):
                print()
                print()
                print("chance : {}".format(self.chances))

                t1 = Timer(10, self.timer)
                t1.start()

                self.t=1
                self.guess=input("enter value : ")
                t1.cancel()
                if(self.t==0):
                    continue

                if (not self.guess.isalpha() ) : # checking for other characters than alphabet
                    print("enter only alphabet!! ")
                    continue
                elif(len(self.guess)>1): # if the length of guess is more than one
                    print("enter only single alphabet")
                    continue
                elif(self.guess in self.letter_guess): # means we have already entered that character
                    print("you have already entered this lettter!!")
                    continue
                if(self.guess in self.word):
                    self.count=self.word.count(self.guess)  #counting the occurence of guess letter in word
                    for _ in range(self.count):  # appending the character to count times
                        self.letter_guess+=self.guess


                self.chances -= 1 # chance will decrease if the guess letter either not correct or correct

                ## printing the characters
                print("\t\t\t\t", end="")
                for char in self.word:
                    """
                     this condition will check two things 
                     1. whether char is in letter_guess .
                     
                     2. is the letter_guess has all character of word 
                        if this happen this mean the word has been found.. 
                    
                        here Countor is used which is container and return  the  
                        a countor object which contain key : value pair
                        where value is each letter in given arg 
                        and value is the number of times that char occur.
                         
                        so if Countor(letter_guess)==Countor(word) this means that
                        letter_guess has all letter in word hence the word has been found 
                     """
                    if(char in self.letter_guess and Counter(self.letter_guess) != Counter(self.word)):

                        print("{:>7}".format(char),end="")
                    # if the word has been found
                    elif(Counter(self.letter_guess)==Counter(self.word) ):
                        print(" {} ".format(self.word))
                        print("bravo you won !!!!!!!!!!!")
                        self.ans=1 # word has found
                        break

                    else:

                        print("{:>7}".format("_"),end="")
                if(self.ans==1): # when we have found the word but chances are remaning thencoming out of while loop
                    #print(self.ans)
                    break

                if(self.chances<=0):
                    print()
                    print("you lost !! try again")
                    print("the word was  : {}".format(self.word))

            # handling when time out during last chance
            if(self.chances==0 and self.ans!=1):
                print("you lost !! try again")
                print("the word was  : {}".format(self.word))

        except (KeyboardInterrupt ,EOFError,RuntimeError) as obj:
            print("something wrong happened!!!!!")
            print("Bye try again !!!")
            print(obj)
            exit()




e=Event()
obj1=hangman()
#print(obj1.lst)

obj1.start_game()


