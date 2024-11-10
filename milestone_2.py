import random as r

from display_hangman import display

# WIP
word_list = ['jackfruit', 'strawberry', 'mango', 'peach', 'nectarine']


# This section contains lists of phrases that add some flavour to the prompts.
game_word = r.choice(word_list)
input_prompt = r.choice(["Enter a letter, chief. ","What do you think...? ", "What have we got, then? ", "What's up next? ", "Go ahead... "])
good_guess = r.choice(["That will do. ","I suppose... ", "Fine. ", "Let's see here... "])
correct_guess = r.choice(["Very good... ", "You live yet... ", "Interesting... ", "Hmm. You got one. "])
wrong_guess = r.choice(["Afraid it's not in the word... ", "Ahh, so close. ", "Not this one... ", "Ouch. No. "])
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
        pass



def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(lets_play)
    print(display(tries))
    print (f"\n\t\t{word_completion}\n")


play('falafel')
user_get_letter_guess()