#Importing random as a function
import random
#assigning a variable to the called int between 1 and 50 
secret_number = random.randint(1, 50)
#This is for debugging purposes
# print(secret_number)
correct_guess = secret_number
#Counter variables for number of guesses
counter = 0 
max_input = 5

print("Guess my secret number.")
#Start of loop connected to the counter. 
while counter < max_input:
#It is always good to have try and except to catch errors. Then we are able to continue past the errors stated in except
    try:
        guess = int(input("Input a number between 1 and 50, you have 5 guesses: \n"))
# adding to counter for each loop
        counter += 1
#If guess is correct then loop breaks here
        if guess == correct_guess:
            print("Great job", guess, "is correct")
            break
#Use of absolute numbers *abs* to give hints for how close or far off the guess was
        elif abs(guess - correct_guess) ==1:
            print("you are insanely close now!")
        elif abs(guess - correct_guess) <= 5:
            print("You are just off by 5 more or less, so pretty close")
        elif abs(guess - correct_guess) <= 10:
            print("You are really close now! about +-10 off")    
        elif guess > correct_guess:
            print("Guess a lot lower")
        else:
            print("Guess a lot higher")
    except ValueError:
        print("Please enter a number!")
#This finishs the game if the counter runs out and you have not guessed correctly
if guess != correct_guess and counter == max_input:
#FOR SOME REASON MY MACBOOK AIR WONT LET ME RUN (f"") so i just used the simple way to show the answer
    print(f"Sorry GAME OVER {correct_guess} is the correct number")
