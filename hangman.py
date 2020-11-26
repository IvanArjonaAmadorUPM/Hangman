# This is the main file to start the game
# You may add any additional modules and other files you wish
import random

class Word:
    tried_words= []
    tried_letters= []
    wordToGuess=""
    word_completion=""

    def __init__(self,word,secretWord):
        self.wordToGuess=word
        self.word_completion=secretWord

    def newLetter(self,a):
        self.tried_letters.append(a)
    def newWords(self,b):
        self.tried_words.append(b)
    def checkLetter(self,a):
        for x in range(0,len(self.tried_letters)):
            if self.tried_letters[x]==a: 
                return True
        return False
    def checkWord(self,a):

        for x in self.tried_words:
            if x==a: 
                return False
        return True        
    def lookLetter(self,a):
        for x in self.wordToGuess:
            if x==a: return True
        return False
    def lookWord(self,a):
        if a == self.wordToGuess: return True
        else: return False

def get_word():
    with open('words.txt', 'r') as file:
        text = file.read().split()
        word=random.choice(text)
        return(word.upper())
        
def isCharacter(guess):
    return len(guess) == 1 and guess.isalpha() 


def hangman(errors):
    hangmanPics = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
         ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
    print (hangmanPics[errors])
def startGame():
    print(" _    _   ____  __    ___  _____  __  __  ____      ____  _____")
    print("( \/\/ ) ( ___)(  )  / __)(  _  )(  \/  )( ___)    (_  _)(  _  )")
    print( " )    (   )__)  )(__( (__  )(_)(  )    (  )__)       )(   )(_)( ")
    print("(__/\__) (____)(____)\___)(_____)(_/\/\_)(____)     (__) (_____)")
    print(" ______  __ __    ___      __ __   ____  ____    ____  ___ ___   ____  ____  ")
    print("|      ||  |  |  /  _]    |  |  | /    ||    \  /    ||   |   | /    ||    \ ")
    print("|      ||  |  | /  [_     |  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |")
    print("|_|  |_||  _  ||    _]    |  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |")
    print("  |  |  |  |  ||   [_     |  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |")
    print("  |  |  |  |  ||     |    |  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |")
    print("  |__|  |__|__||_____|    |__|__||__|__||__|__||___,_||___|___||__|__||__|__|\n\n")
def youLoose():
    print(" __     ______  _    _   _      ____   ____   _____ ______ ")
    print(" \ \   / / __ \| |  | | | |    / __ \ / __ \ / ____|  ____|       +---+")
    print("  \ \_/ / |  | | |  | | | |   | |  | | |  | | (___ | |__          O   |")
    print("   \   /| |  | | |  | | | |   | |  | | |  | |\___ \|  __|        /|\  |")
    print("    | | | |__| | |__| | | |___| |__| | |__| |____) | |_ __       / \  |")
    print("    |_|  \____/ \____/  |______\____/ \____/|_____/|______|          ===")
    print("")
    print("")

def youWin():
    print(" __  ______  __  __  _      _______  __")
    print(" \ \/ / __ \/ / / / | | /| / /  _/ |/ /")
    print("  \  / /_/ / /_/ /  | |/ |/ // //    / ")
    print("  /_/\____/\____/   |__/|__/___/_/|_/  ")
    print("")
    print("")
def seeYou():
    print("███████ ███████ ███████     ██    ██  ██████  ██    ██ ")
    print("██      ██      ██           ██  ██  ██    ██ ██    ██ ")
    print("███████ █████   █████         ████   ██    ██ ██    ██ ")
    print("     ██ ██      ██             ██    ██    ██ ██    ██ ")
    print("███████ ███████ ███████        ██     ██████   ██████  ")

    
def game():
    continuePlaying=True
    
    
    while continuePlaying:
        startGame()
        NewWord=get_word()
        secretWord="."*len(NewWord)
        WordToPlay=Word(NewWord,secretWord)

        WordToPlay.tried_letters.clear()
        WordToPlay.tried_words.clear()

        auxiliarWord=list(WordToPlay.word_completion)
        
        errors=0
        isNotFinished=True

        #print(WordToPlay.wordToGuess)
        while isNotFinished:
            if errors==6:
                youLoose()
                isNotFinished=False
                print("The word was",WordToPlay.wordToGuess)
                break
            if WordToPlay.lookWord(WordToPlay.word_completion):
                youWin()
                print("You won with", errors , "errors")
                isNotFinished=False
                break

            hangman(errors)
            print(WordToPlay.word_completion)

            guess = input("Introduce your guess: ").upper()


            if len(guess)!=len(WordToPlay.wordToGuess) and len(guess)>1:
                print("The length of the word is not the same")
                pass
            if len(guess)== len(WordToPlay.wordToGuess): 
                if WordToPlay.checkWord(guess):
                    if WordToPlay.lookWord(guess): 
                        youWin()
                        print("You won with", errors , "errors")
                        isNotFinished=False
                        break
                    else: 
                        print("That word is not the correct answer!")
                        errors=errors+1
                        WordToPlay.newWords(guess)
                else:
                    print(WordToPlay.tried_words)
                    print("You have already tried this word")
                    pass
            else:
                if isCharacter(guess):
                    if WordToPlay.checkLetter(guess):
                        print("You have already tried this letter")
                        print(WordToPlay.tried_letters)
                        pass
                    else:
                        if WordToPlay.lookLetter(guess):
                            WordToPlay.newLetter(guess)
                            print("the letter is in the word")

                            for i, l in enumerate(WordToPlay.wordToGuess):
                                if l == guess: 

                                    auxiliarWord.pop(i)
                                    auxiliarWord.insert(i,guess)
                            WordToPlay.word_completion="".join(auxiliarWord)

                        else:
                            print("That letter is not included!")
                            WordToPlay.newLetter(guess)
                            errors=errors+1
                else: 
                    print("the letter introduced is not a correct character")
                    pass
        
        x=input("do you want to continue playing?  yes/no\n")
        if x!="yes": continuePlaying = False

    seeYou()
   
    
game()