print("    _    _\n"
      "   | |  | |\n"
      "   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n"
      "   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ \n"
      "   | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n"
      "   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|\n"
      "                        __/ |\n"
      "                       |___/")

wordToGuess=""
tries=0
letterGuessed=[]
guessLength=0
def main():
    global wordToGuess
    wordToGuess=secret_word()
    global tries
    while tries!=7 and guessLength!=len(wordToGuess):
      guess = input("enter a letter ").lower()
      valid=is_input_valid(guess)
      if valid:
         if guess not in wordToGuess:
             tries+=1
             hangman_mode()
             print("Wrong guess, you have %s tries" % (7-tries))
             print(show_secret_word())
         else:
             print("Good guess!\n",show_secret_word())
    print("GAME OVER!\n Results:")
    hangman_mode()
    print("tries",tries)
    print(wordToGuess)
    print(letterGuessed)
    print(show_secret_word())


def is_input_valid(guess):#checks for syntax error, and updates the letterGuessed array with the letters that have been guessed
    if len(guess) == 1 and not 'a' <= guess <= 'z':
        print("Your guess should consist of english letters only")
        return False
    elif len(guess) > 1:
         print("Your guess is too long, 1 character at a time")
         return False
    elif guess in letterGuessed:
        print("You already guessed that...")
        return False

    letterGuessed.append(guess)
    return True


def show_secret_word(): #shows the placement of the letters that the user guessed
    wordToShow=[" _ "]*len(wordToGuess)
    isGuessWordFound = 0
    for i in range(len(letterGuessed)):
        for j in range(len(wordToGuess)):
            if letterGuessed[i]==wordToGuess[j]:
                wordToShow[j]=letterGuessed[i]
                isGuessWordFound+=1
    global guessLength
    if isGuessWordFound>guessLength:
        guessLength=isGuessWordFound
    return "".join(wordToShow)

def hangman_mode():
    dictForPhoto={1:"x-------x",2:" x-------x \n""|\n""|\n""|\n""|\n""|\n",3:"x-------x\n |       |\n |       0\n |\n |\n |",4:" x-------x\n |       |\n |       0\n |       |\n |\n |",5:" x-------x\n |       |\n |       0\n |      /|\\\n |\n |",6:" x-------x\n |       |\n |       0\n |      /|\\\n |      /\n |",7:" x-------x\n |       |\n |       0\n |      /|\\\n |      / \\\n |"}
    global tries
    if tries ==1:
        print(dictForPhoto[1])
    elif tries==2:
        print(dictForPhoto[2])
    elif tries==3:
        print(dictForPhoto[3])
    elif tries==4:
        print(dictForPhoto[4])
    elif tries == 5:
        print(dictForPhoto[5])
    elif tries==6:
        print(dictForPhoto[6])
    elif tries==7:
        print(dictForPhoto[7])

def secret_word():
    indexForWord=int(input("Hello! enter a number \n"))
    indexForWord = (indexForWord-1)%4+1 #4 is the current words
    indexToMatch=0
    with open(r"c:\users\mop\Desktop\check.txt","r") as openFile:
      for line in openFile:
          indexToMatch+=1
          if indexToMatch==indexForWord:
           return line.strip()








if __name__=="__main__":
    main()
