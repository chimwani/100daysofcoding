import random
wordlist = ["camel", "goat", "baboon"]
chosen_word = random.choice(wordlist)
print(chosen_word)
placeholder=""
wordlength=len(chosen_word)
game_over = False
for position in range (wordlength):
        placeholder+="_"
print(placeholder)
while not game_over:
    guess = input("guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        # print(f"Checking letter: {letter}")  # Debug print
        if letter == guess:
            display += guess
        else:
            display += "_"
    print(display)