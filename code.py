import sys
import random


def magic8():

    ans = True

    while ans:
        question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
        
        answers = random.randint(1,8)
        
        if question == "":
            sys.exit()
        
        elif answers == 1:
            print "It is certain"
        
        elif answers == 2:
            print "Outlook good"
        
        elif answers == 3:
            print "You may rely on it"
        
        elif answers == 4:
            print "Ask again later"
        
        elif answers == 5:
            print "Concentrate and ask again"
        
        elif answers == 6:
            print "Reply hazy, try again"
        
        elif answers == 7:
            print "My reply is no"
        
        elif answers == 8:
            print "My sources say no"


def guess():
    import random
    n = random.randint(1, 99)
    guess = int(raw_input("Enter an integer from 1 to 99: "))
    while n != "guess":
        print
        if guess < n:
            print "guess is low"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print "guess is high"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        else:
            print "you guessed it!"
            break
        print


guess()