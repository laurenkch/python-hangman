import random
import string

list_of_secret_words = ['boot','trout','wilt','held','eddy','error','mean','earth','make','array']
list_length = len(list_of_secret_words)
secretWord = list_of_secret_words[random.randint(0,list_length-1)]
word_display =[]
guessed_letters = []
word_length = len(secretWord)
available_letters = list(string.ascii_lowercase)
count = 8

for letter in secretWord:
    word_display.append('_')

def display_word_status():
    for count, letter in enumerate(secretWord):
        if letter in guessed_letters:
            word_display[count] = letter


print(
    f"\nTo play this game, you'll need to guess the letters of a word in {count} tries or less.\nThe secret word has {word_length} letters.\n{word_display}\n")

while count >= 0:

    if '_' not in word_display:
        print("Congratulations. You've won!")
        break

    if count == 0:
        print('You lost :(. Better luck next time. ')
        break

    guess = input('Guess a letter \n').lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}. Try a different letter.\n")
        continue
    guessed_letters.append(guess)
    available_letters.remove(guess)
    
    if guess in secretWord:
        display_word_status()
        print(f'\ngood guess!\n{word_display}\n')
    else:
        print(f'\nNot in this word.\n{word_display}\n')

    count -= 1
    if count > 1:
        print(f'You have {count} guesses remaining')
    else:
        print(f'You have 1 guess remaining')
    print(
        f'\nAvailable Letters:\n{available_letters}\n')


