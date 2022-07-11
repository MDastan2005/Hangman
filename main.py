from constants import HANGMAN_PICS  # import pictures
import random
import string


class IncorrectLetterError(Exception):
    def __init__(self, message="The character is not a letter."):
        super().__init__(message)


class UnknownChoiceError(Exception):
    def __init__(self, choice, message="unknown choice"):
        self.choice = choice
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.choice} is unknown choice. You can choose only between y (yes) and n (no)."


# read words from file
with open("words.txt") as f:
    words = f.read().split("\n")


run = True

# main loop
while run:
    word = random.choice(words)  # get random word from words list
    guess_word = "*" * len(word)  # guess word
    letters = string.ascii_lowercase
    state = 0

    # One round's loop. Runs until we guess the word or die.
    while state < len(HANGMAN_PICS) - 1 and not guess_word.isalpha():
        print(guess_word)
        print(HANGMAN_PICS[state])  # printing picture
        print()
        print(*letters, sep=' ')  # printing available characters

        # player choose a letter
        letter = input('Choose a letter: ')
        while letter not in letters:
            if letter not in string.ascii_lowercase:
                raise IncorrectLetterError
            letter = input('Choose a letter: ')

        # check if the letter is correct
        letters = letters.replace(letter, '')
        if letter in word:
            for idx, c in enumerate(word):
                if c == letter:
                    guess_word = guess_word[:idx] + letter + guess_word[idx + 1:]
            print("\n\n")
            print("NICE!\nCorrect letter")
            print("\n\n")
        else:
            state += 1

    # print result of the game
    if state == len(HANGMAN_PICS) - 1:
        print("\n\n\n\n")
        print("YOU LOSE!")
        print("\n\n\n\n")
    elif guess_word.isalpha():
        print("\n\n\n\n")
        print("CONGRATULATIONS!\nYOU WIN!")
        print("\n\n\n\n")

    # ask is player want play again
    choice = input("Want to play again? (y/n): ")
    match choice:
        case 'n':
            break
        case 'y':
            continue
        case other:
            raise UnknownChoiceError(other)
