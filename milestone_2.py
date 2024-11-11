import random as r
import requests

from display_hangman import display

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
word_list = response.text.splitlines()
long_words = [word for word in word_list if len(word) > 2]


game_word = r.choice(long_words).upper()

# This section contains lists of phrases that add some sassy flavour to the prompts.
# These get called using random.choice() in the functions below.
input_prompt = (["Enter a letter, chief. ","What do you think...? ", "What have we got, then? ", "What's up next? ", "Go ahead... "])
valid_guess = (["That will do. ","I suppose... ", "Fine. ", "Let's see here... "])
# Whereas correct means the letter is in the word.
correct_guess = (["Very good... ", "You live yet... ", "Interesting... ", "Hmm. You got one. "])

wrong_guess = (["Afraid it's not in the word... ", "Ahh, so close. ", "Not this one... ", "Ouch. No. "])


invalid_guess = (["Not sure that's one letter...", "No. That won't work. Guess one letter. ", "I don't think so, chief. Try a single letter. ", "Nu-uh."])

lets_play = (["Are you ready then?", "Let's try your luck.", "Back again, are we...", "Let's see how you get on this time..."])
lost_game = (["Too bad, bucko. You'll get 'em next time.", "How unfortunate. Maybe next time.", "Well well. You gave it your best. Perhaps you'll try again.", "So close. Better luck next time."])
won_game = (["Looky here, you actually pulled it off.", "Colour me impressed. Well played.", "That's the one... well done. Another?"])


def user_get_letter_guess():
    while True:
        guess = input(r.choice(input_prompt))
        if is_valid_guess(guess) == True:
            # print(r.choice(valid_guess)) - redundant
            return guess.upper()

        else:
            print(r.choice(invalid_guess))
    

def is_valid_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        return False
        
def guess_in_word(guess):
    if guess in game_word:
        return True
    else:
        return False



def play(word):
    # This function contains the whole logic for the Hangman game.
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts_left = 6
    print(r.choice(lets_play))
    print(display(attempts_left))
    print (f"\n\t\t{word_completion}\n")
    while not guessed and attempts_left > 0:
        guess = user_get_letter_guess()
        if guess in guessed_letters:
            print(f"You already tried {guess}.")
        elif guess not in word:
            print(r.choice(wrong_guess))
            attempts_left -= 1
            guessed_letters.append(guess)
            print(display(attempts_left))
            print (f"\n\t\t{word_completion}\n")
            print(f"\n\tAlready guessed: {[l for l in guessed_letters if l not in word]}\n")
# TODO maybe:
# add elif for guessing words
        else:
            print(r.choice(correct_guess))
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            print(display(attempts_left))
            print (f"\n\t\t{word_completion}\n")
            print(f"\n\tAlready guessed: {[l for l in guessed_letters if l not in word]}\n")
            if "_" not in word_completion:
                guessed = True
    if attempts_left == 0:
        word_completion = word
        print(display(attempts_left))
        print (f"\n\t\t{word_completion}\n")
        print(r.choice(lost_game))
    if guessed == True:
        print(f"\n{r.choice(won_game)}")
            


def main():
    word = r.choice(long_words).upper()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = r.choice(long_words).upper()
        play(word)

if __name__ == "__main__":
    main()
        





