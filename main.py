import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "house", "igloo", "jacket"]
    return random.choice(word_list)

def display_hint(word, revealed_letters):
    hint = ""
    for letter in word:
        if letter in revealed_letters:
            hint += letter
        else:
            hint += "_"
    return hint

def play_game():
    print("Welcome to the Random Word Guessing Game!")
    
    while True:
        secret_word = choose_random_word()
        revealed_letters = []
        attempts = 5
        
        while attempts > 0:
            hint = display_hint(secret_word, revealed_letters)
            print(f"Word: {hint}")
            guess = input("Enter your guess: ").lower()
            
            if guess == secret_word:
                print("Congratulations! You guessed the word correctly.")
                break
            elif guess in secret_word:
                print("Good guess! That letter is in the word.")
                revealed_letters.append(guess)
            else:
                attempts -= 1
                print(f"Sorry, that's not the word. You have {attempts} attempts left.")
        
        if attempts == 0:
            print(f"Out of attempts! The word was '{secret_word}'. Better luck next time!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
