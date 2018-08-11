import random
print('Please, enter your name!')
name = input()
secret_num = random.randint(1, 20)
print('Well, {}. I am thinking of a number between 1 and 20'.format(name))

for guesses_taken in range(1, 7):
    print('Take a guess.')
    try:
        given_num = int(input())
        if given_num > secret_num:
            print('Your guess is too high')
        elif given_num < secret_num:
            print('Your guess is too low')
        else:
            print('Good job {}! You guessed my number in {} guesses'.format(name, guesses_taken))
            break
    except:
        print('You did not enter a number')
   
try:
    if given_num != secret_num:
        print('Nope. The number i was thinking was {}'.format(secret_num))
except NameError:
    print('Nope. The number i was thinking was {}'.format(secret_num))
