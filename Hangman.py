'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''


def find_index(letter, word_to_guess):
    indexes = []
    for i in range(len(word_to_guess)):
        if letter == word_to_guess[i]:
            indexes.append(i)
    return indexes


def replace_letters(word_to_guess, letter, word_):
    index_list = find_index(letter, word_to_guess)
    word_list = list(word_)
    for i in index_list:
        word_list[i] = letter
    return "".join(word_list)


def hangman_game(word_to_guess):
    tries = 6
    letters_list = []
    lack_words = len(word_to_guess) * "_"
    while tries <= 6 and tries > 0:
        print(f"You have {tries} tries left.")
        letters_list_string = " ".join(letters_list)
        print(f"Used letters: {letters_list_string} ")
        print(f"Word: {lack_words}")
        guess_letter = input("Guess a letter: ")
        lack_words = replace_letters(word_to_guess, guess_letter, lack_words)
        print("               ")
        letters_list.append(guess_letter)
        if guess_letter not in word_to_guess:
            tries -= 1
        if word_to_guess == lack_words:
            print(f"You guessed the word {word_to_guess}!")
            break
        if tries == 0:
            print("Game over!" + f"The word is: {word_to_guess}")


if __name__ == "__main__":
    hangman_game("anabella")
