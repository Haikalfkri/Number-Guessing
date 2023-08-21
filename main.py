import random

# make random number between 1 to 30
random_number = random.randint(1, 30)

# Login end
end = False

# make health / or how many times that user can make wrong guess
health = 5

print("Guess a number between 1 to 30 and you just have only 5 health")

# make while loop if end != True
while not end:
    
    # get user input as int
    user_input = int(input("Guess the number: "))
    
    if health != 1:
        # condition for check user input and random number 
        if user_input < random_number:
            print("Too low")
            health -= 1
            print(f"You have {health} left")
        if user_input > random_number:
            print("Too high")
            health -= 1
            print(f"You have {health} left")
        if user_input == random_number:
            print("Your right")
            end = True
    else:
        print('You out of health')
        end = True