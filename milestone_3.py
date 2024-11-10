from milestone_2 import user_get_letter_guess

guess = 

while True:

    # Step 3: Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        break  # Step 4: Exit the loop if the guess passes the checks
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

        