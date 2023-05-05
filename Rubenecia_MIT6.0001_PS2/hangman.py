# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    list_word = list(secret_word)
    counter = 0
    for var in secret_word:
        for char in letters_guessed:
            if char == var:
                counter += 1
                break
            else:
                pass
        else:
            pass
    if counter == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed = set(letters_guessed)
    letters_guessed = list(letters_guessed)
    word_guess = []
    for i in range(len(secret_word)):
        word_guess.append('_')
        for j in range(len(letters_guessed)):
            if secret_word[i] == letters_guessed[j]:
                word_guess[i] = letters_guessed[j]
                break
            else:
                pass

    return "".join(word_guess)





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_guessed = set(letters_guessed)
    blank = ""
    for char in letters_guessed:
        if alphabet.__contains__(char):
            alphabet.remove(char)
        else:
            pass
    return blank.join(alphabet)


    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    initial_guess = 6
    guesses = initial_guess
    print("Welcome to the game Hangman!!!!")
    print(f"I'm thinking of a word that is   {len(secret_word)} letters long")
    print(secret_word)
    guess_letter_list = [' ']
    secret_word_list = list(secret_word)
    guess_word = get_guessed_word(secret_word, guess_letter_list)
    warning_counter = 3
    while True:
        print("______________________________________")
        guess_word = get_guessed_word(secret_word, guess_letter_list)
        available_letters = get_available_letters(guess_letter_list)
        if guesses == 0:
            print("Sorry you run out of guesses")
            break
        if warning_counter == 0:
            guesses = 0
            print(f"You have no warnings left so based on rules you're booted out the game")
            break
        if secret_word == guess_word:
            print(f"YOU HAVE GUESS THE WORD: {secret_word}")
            break
        print(f"Guesses left: {guesses}")
        print(f"Word: {guess_word}")
        print(f"Available letters: {available_letters}")
        guess_letter = input("Guess a letter: ")

        if guess_letter.__len__() !=1 & guess_letter.isalpha():
            print("Please input 1 character and a letter of the english alphabet only."
                  f"{warning_counter-1} warnings left or else you will automatically lose")
            print(guess_word)
            warning_counter -= 1
            continue

        else:
            pass
        guess_letter.lower()
        if guess_letter_list.__contains__(guess_letter):
            print(f"You have already inputted that letter please try another one. {warning_counter-1} "
                                 f"warnings left or else you will automatically lose ")
            print(guess_word)
            warning_counter -= 1
            continue
        else:
            pass
        guess_letter_list.append(guess_letter)
        if not secret_word_list.__contains__(guess_letter):
            print(f"Oops! That letter is not in my Word: {guess_word}")
            guesses -= 1
        else:
            pass

    secret_word_unique = set(secret_word_list)
    total_score = len(secret_word_unique)*guesses
    print(f"THE GAME HAS ENDED,")
    if total_score >= len(secret_word):
        print(f"CONGRATULATION IN WINNING THE GAME!!!, YOUR TOTAL SCORE IS: {total_score}")
    else:
        print(f"YOU LOSE BETTER LUCK NEXT TIME............")
















# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    match = False
    if len(my_word) == len(other_word):
        match = True
        for i in range(len(other_word)):
            if my_word[i] != '_' and my_word[i] != other_word[i]:
                match = False
                break
    if match:
        return True
    else:
        return False





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []

    for words in wordlist:
        if match_with_gaps(my_word, words):
            matches.append(words)
    if not matches:
        return "No matches found"
    else:
        return matches





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    initial_guess = 6
    guesses = initial_guess
    print("Welcome to the game Hangman!!!!")
    print(f"I'm thinking of a word that is   {len(secret_word)} letters long")
    print(secret_word)
    guess_letter_list = [' ']
    secret_word_list = list(secret_word)
    guess_word = get_guessed_word(secret_word, guess_letter_list)
    warning_counter = 3
    while True:
        print("______________________________________")
        guess_word = get_guessed_word(secret_word, guess_letter_list)
        available_letters = get_available_letters(guess_letter_list)
        if guesses == 0:
            print("Sorry you run out of guesses")
            break
        if warning_counter == 0:
            guesses = 0
            print(f"You have no warnings left so based on rules you're booted out the game")
            break
        if secret_word == guess_word:
            print(f"YOU HAVE GUESS THE WORD: {secret_word}")
            break
        print(f"Guesses left: {guesses}")
        print(f"Word: {guess_word}")
        print(f"Available letters: {available_letters}")
        guess_letter = input("Guess a letter: ")

        if guess_letter == '*':
            print(show_possible_matches(guess_word))
            continue

        if guess_letter.__len__() != 1 & guess_letter.isalpha():
            print("Please input 1 character and a letter of the english alphabet only."
                  f"{warning_counter - 1} warnings left or else you will automatically lose")
            print(guess_word)
            warning_counter -= 1
            continue

        else:
            pass
        guess_letter.lower()
        if guess_letter_list.__contains__(guess_letter):
            print(f"You have already inputted that letter please try another one. {warning_counter - 1} "
                  f"warnings left or else you will automatically lose ")
            print(guess_word)
            warning_counter -= 1
            continue
        else:
            pass
        guess_letter_list.append(guess_letter)
        if not secret_word_list.__contains__(guess_letter):
            print(f"Oops! That letter is not in my Word: {guess_word}")
            guesses -= 1
        else:
            pass

    secret_word_unique = set(secret_word_list)
    total_score = len(secret_word_unique) * guesses
    print(f"THE GAME HAS ENDED,")
    if total_score >= len(secret_word):
        print(f"CONGRATULATION IN WINNING THE GAME!!!, YOUR TOTAL SCORE IS: {total_score}")
    else:
        print(f"YOU LOSE BETTER LUCK NEXT TIME............")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
