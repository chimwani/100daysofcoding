import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
#TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder=""
for position in range(len(chosen_word)):
    placeholder+="-"
print(placeholder)
guess=input("guess a letter: ").lower()
for letter  in chosen_word:
    if guess== letter:
        print("right")
    else:
        print("wrong")
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display=[]
for _ in chosen_word:
    display.append("-")
    print(display)