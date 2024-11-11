import random as r
import requests

from display_hangman import display

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
word_list = response.text.splitlines()
long_words = [word for word in word_list if len(word) > 2]


# game_word = r.choice(long_words).upper()

# This section contains lists of phrases that add some sassy flavour to the prompts.
# These get called using random.choice() in the functions below.
input_prompt = (["Enter a letter, chief. ","What do you think...? ", "What have we got, then? ", "What's up next? ", "Go ahead... "])
valid_guess = (["That will do. ","I suppose... ", "Fine. ", "Let's see here... "])
correct_guess = (["Very good... ", "You live yet... ", "Interesting... ", "Hmm. You got one. "])
wrong_guess = (["Afraid it's not in the word... ", "Ahh, so close. ", "Not this one... ", "Ouch. No. "])
invalid_guess = (["Not sure that's one letter...", "No. That won't work. Guess one letter. ", "I don't think so, chief. Try a single letter. ", "Nu-uh."])
lets_play = (["Are you ready then?", "Let's try your luck.", "Back again, are we...", "Let's see how you get on this time..."])
lost_game = (["Too bad, bucko. You'll get 'em next time.", "How unfortunate. Maybe next time.", "Well well. You gave it your best. Perhaps you'll try again.", "So close. Better luck next time."])
won_game = (["Looky here, you actually pulled it off.", "Colour me impressed. Well played.", "That's the one... well done. Another?"])


class Hangman:
    def __init__(self, game_word: str):
        self.game_word = game_word.upper()
        self.word_completion = "_" * len(self.game_word)
        self.guessed = False
        self.guessed_letters = []
        # self.guessed_words = []
        self.attempts_left = 6

    def is_valid_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            return True
        else:
            return False
        
    def user_get_letter_guess(self):
        while True:
            guess = input(r.choice(input_prompt))
            if self.is_valid_guess(guess) == True:
                # print(r.choice(valid_guess)) - redundant
                return guess.upper()

            else:
                print(r.choice(invalid_guess))
            
    def guess_in_word(self, guess):
        if guess not in self.game_word:
            print(r.choice(wrong_guess))
            self.attempts_left -= 1
            self.guessed_letters.append(guess)
            print(display(self.attempts_left))
            print (f"\n\t\t{self.word_completion}\n")
            print(f"\n\tAlready guessed: {[l for l in self.guessed_letters if l not in self.game_word]}\n")
        else:
                print(r.choice(correct_guess))
                self.guessed_letters.append(guess)
                word_as_list = list(self.word_completion)
                indices = [i for i, letter in enumerate(self.game_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                self.word_completion = "".join(word_as_list)
                print(display(self.attempts_left))
                print (f"\n\t\t{self.word_completion}\n")
                print(f"\n\tAlready guessed: {[l for l in self.guessed_letters if l not in self.game_word]}\n")
        



    def play(self):
        # This function contains the whole logic for the Hangman game.

        print(r.choice(lets_play))
        print(display(self.attempts_left))
        print (f"\n\t\t{self.word_completion}\n")
        while not self.guessed and self.attempts_left > 0:
            guess = self.user_get_letter_guess()
            if guess in self.guessed_letters:
                print(f"You already tried {guess}.")
            self.guess_in_word(guess)

            if "_" not in self.word_completion:
                    self.guessed = True

        if self.attempts_left == 0:
            self.word_completion = self.game_word
            print(display(self.attempts_left))
            print (f"\n\t\t{self.word_completion}\n")
            print(r.choice(lost_game))
        if self.guessed == True:
            print(f"\n{r.choice(won_game)}")
            


def main():
    game_word = r.choice(long_words).upper()
    game = Hangman(game_word)  # Create an instance of Hangman with game_word
    game.play()  
    while input("Play again? (Y/N) ").upper() == "Y":
        game_word = r.choice(long_words).upper()
        game = Hangman(game_word)  # Create a new instance for each new game
        game.play()

if __name__ == "__main__":
    main()

        





