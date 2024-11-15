import random as r
import requests
'''
This is an entirely CLI-based game of Hangman, where you try to guess a random word one character at a time.
It has a simple, clear visual, some neat quality of life features, and a healthy helping of sass.

`display(attempts_left)` is an ASCII based visual representation of our soon to be hanged fella,
indicating how many lives/attempts the player has left.
It is a list of strings, indexed so each visual represents the number of lives left.
'''
from display_hangman import display

word_site = "https://www.mit.edu/~ecprice/wordlist.10000" # contains swearwords
response = requests.get(word_site)
word_list = response.text.splitlines()
long_words = [word for word in word_list if len(word) > 3]

'''
Here we import a dictionary of various phrases, that add sassy flavour to our gamesmaster.
We then call them using `random.choice` throughout the script.
'''
from phrases import phrases
def phrase(phrase_type):
    print(r.choice(phrases[phrase_type]))

class Hangman:
    '''
    This makes up the bulk of the game's logic.
    `word_completion` is the game_word represented with '_' underscores.
    `guessed` is a boolean state defining whether the games has been won.
    `attempts_left` is the player's lives, 6 by default, can go between 1-9.
    '''
    def __init__(self, game_word: str, attempts_left: int = 6):
        self.game_word = game_word.upper()
        self.word_completion = "_" * len(self.game_word) # TODO can be list comprehension 
        self.guessed = False
        self.guessed_letters = []
        self.attempts_left = attempts_left

    def is_valid_guess(self, guess):
        # We only allow 1-letter guesses.
        if len(guess) == 1 and guess.isalpha():
            return True
        else:
            return False
        
    def user_get_letter_guess(self):
        # We collect a valid user input, making it upper-case.
        while True:
            guess = input(r.choice(phrases['input_prompt']))
            if self.is_valid_guess(guess):
                return guess.upper()
            else:
                phrase('invalid_guess')

    def guess_in_word(self, guess):
        '''
        We replace the underscores in `word_completion` with the letter if the player's guess is in the secret gameword,
        we take off a life and show letters guessed that are not in the word as a nice bit of quality of life.
        '''
        if guess in self.game_word:
            word_as_list = list(self.word_completion)
            for index, letter in enumerate(self.game_word):
                if letter == guess:
                    word_as_list[index] = guess
            self.word_completion = "".join(word_as_list)
            response = phrase('correct_guess')
        else:
            self.attempts_left -= 1
            response = phrase('wrong_guess')
        self.guessed_letters.append(guess)
        print(display(self.attempts_left))
        print(f"\n\t\t{self.word_completion}\n")
        print(f"\n\tAlready guessed: {[l for l in self.guessed_letters if l not in self.game_word]}\n")
        response

    def play(self):
        phrase('lets_play')
        print(display(self.attempts_left))
        print (f"\n\t\t{self.word_completion}\n")
        while not self.guessed and self.attempts_left > 0:
            guess = self.user_get_letter_guess()
            if guess in self.guessed_letters:
                print(f"You already tried {guess}.")
                continue
            self.guess_in_word(guess)
            if "_" not in self.word_completion:
                    self.guessed = True

        if self.attempts_left == 0:
            # Here we reveal the word if the player runs out of lives.
            self.word_completion = self.game_word
            print(display(self.attempts_left))
            print (f"\n\t\t{self.word_completion}\n")
            phrase('lost_game')
        if self.guessed:
            print(f"\n{r.choice(phrases['won_game'])}")
            
def play_game():
    # A while loop to allow the player to 'play again', with a new random game_word.
    game_word = r.choice(long_words)
    game = Hangman(game_word) 
    game.play()  
    while input("Play again? (Y/N) ").upper() == "Y":
        game_word = r.choice(long_words)
        game = Hangman(game_word)
        game.play()

if __name__ == "__main__":
    play_game()

        





