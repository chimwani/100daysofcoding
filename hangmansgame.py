import random
wordlist = ["camel", "goat", "baboon"]
chosen_word = random.choice(wordlist)
print(chosen_word)
placeholder=""
wordlength=len(chosen_word)
game_over = False
lives=6
for position in range (wordlength):
        placeholder+="_"
print(placeholder)
correct_letters = []
while not game_over:
    guess = input("guess a letter: ").lower()
    correctguess = False
    display = ""
    for letter in chosen_word:
        # print(f"Checking letter: {letter}")  # Debug print
        if letter == guess:
            display += guess
            correct_letters.append(letter)
            correctguess=True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if not correctguess:
            lives -=1
            print(f"you have guessed wrong .You have {lives} remaining.")
    print(display)
    if "_" not in display:
        game_over=True
        print("you win")
    if lives==0:
        game_over=True
        print("you lost")
        print(f"the correct word is {chosen_word}")