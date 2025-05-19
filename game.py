from random import randint

n = randint(1, 50)
while True:
    ans = int(input('Enter a guess: '))
    if ans > n:
        print('Too high! Guess again. ')
    elif ans < n:
        print('Too low! Guess again. ')
    else:
        print('Congrats! You got it! ')
        break