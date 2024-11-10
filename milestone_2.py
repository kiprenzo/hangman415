import random as r
import requests

from display_hangman import display

# TODO
# Replace list with list from MIT https://www.mit.edu/~ecprice/wordlist.10000
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
word_list = response.text.splitlines()


# This section contains lists of phrases that add some flavour to the prompts.
game_word = r.choice(word_list)
input_prompt = r.choice(["Enter a letter, chief. ","What do you think...? ", "What have we got, then? ", "What's up next? ", "Go ahead... "])
# A good guess is a valid one.
good_guess = r.choice(["That will do. ","I suppose... ", "Fine. ", "Let's see here... "])
# Whereas correct means the letter is in the word.
correct_guess = r.choice(["Very good... ", "You live yet... ", "Interesting... ", "Hmm. You got one. "])
wrong_guess = r.choice(["Afraid it's not in the word... ", "Ahh, so close. ", "Not this one... ", "Ouch. No. "])
# A bad guess is an invalid one.
bad_guess = (["Not sure that's one letter...", "No. That won't work. Guess one letter. ", "I don't think so, chief. Try a single letter. ", "Nu-uh."])
lets_play = r.choice(["Are you ready then?", "Let's try your luck.", "Back again, are we...", "Let's see how you get on this time..."])

print(game_word.upper())

def user_get_letter_guess():
    while True:
        guess = input(input_prompt)
        if is_valid_guess(guess) == True:
            print(good_guess)
            return guess.upper()

        else:
            print(r.choice(bad_guess))
    

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
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(lets_play)
    print(display(tries))
    print (f"\n\t\t{word_completion}\n")
    while not guessed and tries > 0:
        guess = user_get_letter_guess()
        if guess in guessed_letters:
            print(f"You already tried {guess}.")
        elif guess not in word:
            print(wrong_guess)
            tries -= 1
            guessed_letters.append(guess)
            print(display(tries))
            print (f"\n\t\t{word_completion}\n")
# TODO
# add elif for guessing words
        else:
            print(correct_guess)
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            print(display(tries))
            print (f"\n\t\t{word_completion}\n")
            if "_" not in word_completion:
                guessed = True
            

play("APPLE")
        





