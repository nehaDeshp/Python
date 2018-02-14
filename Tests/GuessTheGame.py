from random import *


class GuessOutOfRange:
    def __init__(self,max):
        print("Value not in range .. Enter range between 0 to %d" %max)

class RandomNumberGenerator:
    def __init__(self,max):
        self.randomNumber = randint(0,max)

class GuessingGame:
    def __init__(self,answer=-1,
                 max=1000,
                 generator=1,
                 gameOver=False,
                 differential=-1,
                 maxGuessesAllowed=max,
                 numGuessesTaken=0):
        self.__max = max
        self.__generator = generator
        self.__answer = answer
        self.__gameOver=gameOver
        self.__maxGuessesAllowed=maxGuessesAllowed
        self.__numGuessesTaken=numGuessesTaken
        self.__differential = differential

    def newGame(self,maxGuessesAllowed):
        self.__maxGuessesAllowed = maxGuessesAllowed
        max = int(input("Enter Maximum Guessing Range"))
        self.setMax(max)
        print("Start a New Game", self.getMax())
        self.__answer = answer = RandomNumberGenerator(self.getMax()).randomNumber
        print(self.getAnswer())
        self.__gameOver = False
        self.__differential=self.getMax()
        self.__numGuessesTaken=0
        self.setAllowedGuess(maxGuessesAllowed)

    def guess(self,newGuess):
        print("Answer is : ",self.getAnswer())
        if(newGuess < self.__max and newGuess >= 0):
            self.setTakenGuess(self.getTakenGuess()+1)
            if(newGuess == self.getAnswer()):
                print("You win")
            else:
                if(newGuess > self.getAnswer()):
                    print("Too High")
                else:
                    print("Too Low")
                if(self.getAllowedGuess() - self.getTakenGuess() >= 0):
                    if(self.getDiff() < abs(newGuess-self.getAnswer())):
                        print("Getting Colder")
                    else:
                        print("Getting Warmer")
                    self.setDiff(abs(newGuess-self.getAnswer()))
        else:
            raise GuessOutOfRange(max)

    def isGameOver(self):
        return self.getTakenGuess() == self.getAllowedGuess() or self.getDiff() == 0

    #Getter and Setter Methods for instance Variables
    def getMax(self):   return self.__max
    def setMax(self,val):   self.__max = val

    def getDiff(self):  return self.__differential
    def setDiff(self,diff): self.__differential=diff

    def getAnswer(self):  return self.__answer
    def setAnswer(self,ans): self.__answer=ans

    def getAllowedGuess(self):  return self.__maxGuessesAllowed
    def setAllowedGuess(self,maxGuess): self.__maxGuessesAllowed=maxGuess

    def getTakenGuess(self):  return self.__numGuessesTaken
    def setTakenGuess(self,numGuess): self.__numGuessesTaken=numGuess

game = GuessingGame()
while True:
    maxGuessesAllowed = int(input("Enter Maximum Guesses allowed"))
    game.newGame(maxGuessesAllowed)
    while game.isGameOver()==False:
        new = int(input("Guess ... "))
        game.guess(new)

    continueGame = input("Would you like to play again, enter Y for yes, N for no: ")
    if "n" or "N" in continueGame:
        print("Thanks for playing!")
        break