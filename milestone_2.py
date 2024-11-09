word_list = ['jackfruit', 'strawberry', 'mango', 'peach', 'nectarine']

print(word_list)

import random as r

word = r.choice(word_list)
input_prompt = r.choice["Enter a letter, chief. ","What do you think...? ", "What have we got, then? ", "What's up next? ", "Go ahead... "]
good_guess = r.choice["That will do.","I suppose...", "Fine.", "Let's see here..."]
bad_guess = r.choice["Not sure about that one. Again. ", "No. That won't work. ", "I don't think so, chief. Try again. ", "Nu-uh."]


print(word)

guess = input(input_prompt)

if len(guess) == 1 and type(guess) == str:
    print(good_guess)
else:
    print(bad_guess)