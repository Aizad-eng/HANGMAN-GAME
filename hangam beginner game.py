import random
import steps
import word
from asciiart import logo
from asciiart import welcome
from asciiart import won
from asciiart import lose
list1 = []

print(logo)
print(welcome)
chosen_word = random.choice(word.word_list)
for _ in range(len(chosen_word)):
    list1.append("_")
lives = 0

end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower() 
    for i in range(len(chosen_word)):
        if guess == list1[i]:
            print(f"You already guessed the letter {guess}")
        if guess in chosen_word[i]:
            list1[i] = guess
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        print(steps.step[lives])
        lives+=1
        if lives == 7:
            end_of_game=True
            print(lose)
            print(f"The correct word was '{chosen_word}'")
    print(list1)
    
    if "_" not in list1:
        end_of_game=True
        print(won)