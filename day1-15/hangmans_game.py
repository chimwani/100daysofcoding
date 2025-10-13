import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
word_length= len(chosen_word)
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for position in range(word_length):
    placeholder+="_"
print (placeholder)

correct_list=[]
game_over=False
while game_over != True:
    
    guess=input("guess a letter:").lower()

    # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    display=""
    for letter in chosen_word:
        if guess == letter:
            display+=guess
            correct_list.append(letter)
        elif letter in correct_list:
            display+=letter
        else:
            display+="_"
    print(display)
  
   
#- If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over = True
            print("you lost")
    
    if "_" not in display:
        game_over = True
        print("you have won")

    print(stages[lives])