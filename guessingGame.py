number = 6
print('This is a game where you have to guess a number in two chances and if you guess it right then you win!')
chooseNumber1 = int(input('Enter the number you want to guess: '))
if(chooseNumber1<=3):
    print('Your guess was too low. Guess a higher number than 3')
    chooseNumber2 = int(input('Enter the number you want to guess: '))
    if(chooseNumber2<=3):
        print('Your guess was too low. You lost!')
    elif(chooseNumber2<=5):
        print('Your guess was low. You lost!')
    elif(chooseNumber2>=7):
        print('Your guess was high. You lost!')
    else:
        print('You guessed the right number. Congratulations you won!!')

elif(chooseNumber1<=5):
    print('Your guess was low. Guess a higher number than 5')
    chooseNumber3 = int(input('Enter the number you want to guess: '))
    if(chooseNumber3<=3):
        print('Your guess was too low. You lost!')
    elif(chooseNumber3<=5):
        print('Your guess was low. You lost!')
    elif(chooseNumber3>=7):
        print('Your guess was high. You lost!')
    else:
        print('You guessed the right number. Congratulations you won!!')
    
elif(chooseNumber1>=7):
    print('Your guess was high. Guess a lower number than 7')
    chooseNumber4 = int(input('Enter the number you want to guess: '))
    if(chooseNumber4<=3):
        print('Your guess was too low. You lost!')
    elif(chooseNumber4<=5):
        print('Your guess was low. You lost!')
    elif(chooseNumber4>=7):
        print('Your guess was high. You lost!')
    else:
        print('You guessed the right number. Congratulations you won!!')
else:
    print('You guessed the right number. Congratulations you won!!')
