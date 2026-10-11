def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        guess_word = "".join(
            char if char in guesses else "_"
            for char in secret_word
        )

        print(guess_word)

        return "_" not in guess_word
    return hangman_closure

secret_word = input("Enter a secret word: ").lower()
game = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ").lower()
    if game(letter):
        print(f"Congratulations! You guessed the word: {secret_word}!")
        break