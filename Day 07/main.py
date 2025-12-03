import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("WELCOME TO THE GAME !")

# Random word to guess
word_to_be_guess = random.choice(hangman_words.word_list)

# Create blank spaces
empty_word = ["_"] * len(word_to_be_guess)

# Track guessed letters
guessed_letters = []

print(" ".join(empty_word))
game_on = True

lives = 6

while game_on:
    guess_letter = input("\nGuess a letter: ").lower()

    # Already guessed
    if guess_letter in guessed_letters:
        print(f"You already guessed '{guess_letter}'. Try another letter.")
        continue
    else:
        guessed_letters.append(guess_letter)

    # If guess is correct
    if guess_letter in word_to_be_guess:
        for i in range(len(word_to_be_guess)):
            if word_to_be_guess[i] == guess_letter:
                empty_word[i] = guess_letter
        print("Good guess!")
        print(hangman_art.stages[lives])
    else:
        print("Wrong guess!")
        lives -= 1
        print(hangman_art.stages[lives])


    # Show current progress
    print(" ".join(empty_word))
    #live remaining
    print(f"\nYOUR LIVES REMAINING :{lives}")
    # Check if all letters guessed
    if "_" not in empty_word:
        game_on = False
        print("\n🎉 You win! The word was:", word_to_be_guess)
    if lives == 0:
        game_on = False
        print("GAME OVER !")










