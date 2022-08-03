import random
import os
from words import list_of_words
from hangman_art import stages, logo

print(logo)
print("------------------------------------------------\n")

#set this true only when the word is fully guessed
end_of_game = False 
#goes through the list and picks a random word 
chosen_word = random.choice(list_of_words).upper()
#assign length to chosen word
word_length = len(chosen_word)
lives = 6
print(f'You start with {lives} lives.\n')
#test print to see the random word
print(chosen_word)

#empty list 
display_word = []

#print '_' for every letter in the chosen word 
for letter in chosen_word:
    display_word += "_"
print(' '.join(display_word))

while not end_of_game:
#input for guess 
    guess = input("\nGuess a letter: ").upper()

    #clears after every attempt
    clear = lambda: os.system('cls')
    clear()
    
    if guess in display_word:
        print(f'\nYou have already guessed {guess}.')

    #this for loop handles the positioning of the blank and position of the letter when guessed correctly
    for position in range(word_length):
        letter = chosen_word[position]
      #  print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display_word[position] = letter
    
    #deals with losing lives
    if guess not in chosen_word:
        lives -= 1
        print(f'\nYou guessed {guess}. That letter is not in the word. You have {lives} lives left.\n')
    print(' '.join(display_word))
    print(stages[lives])

    if lives == 0:
        end_of_game = True
        print("You lose.\n")

    if "_" not in display_word:
        end_of_game = True
        print("You win!\n")