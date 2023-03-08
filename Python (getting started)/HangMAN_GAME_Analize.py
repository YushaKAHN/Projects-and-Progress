import random

# List of words to choose from
words = ['python', 'java', 'ruby', 'javascript',
         'php', 'swift', 'kotlin', 'csharp', 'dart', 'go']

# Function to choose a random word from the list


def choose_word():
    return random.choice(words)

# Function to initialize the game


def initialize(word):
    # Create a list of underscores with the same length as the word
    return ['_'] * len(word)

# Function to play the game


def play(word):
    # Initialize the game
    guessed = initialize(word)
    wrong_guesses = []
    tries = 6

    # Loop until the player has guessed the word or has run out of tries
    while tries > 0 and '_' in guessed:
        # Print the current state of the game
        print(' '.join(guessed))
        print(f'Wrong guesses: {", ".join(wrong_guesses)}')
        print(f'{tries} tries left\n')

        # Get a guess from the player
        guess = input('Guess a letter: ').lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter')
            continue

        # Check if the guess has already been made
        if guess in wrong_guesses or guess in guessed:
            print('You already guessed that letter')
            continue

        # Check if the guess is correct
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            wrong_guesses.append(guess)
            tries -= 1

    # Print the final state of the game
    print(' '.join(guessed))
    if '_' not in guessed:
        print('Congratulations, you guessed the word!')
    else:
        print(f'Sorry, the word was {word}')

# Main function to start the game


def main():
    word = choose_word()
    play(word)


# Start the game
if __name__ == '__main__':
    main()
