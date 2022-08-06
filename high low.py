import random

upper = int(input('Upper bound: \n'))
lower = int(input('Lower bound:\n'))
while lower > upper:
    print('Error: lower value cannot be higher than upper value')
    upper = int(input('Upper bound: \n'))
    lower = int(input('Lower bound:\n'))

randnum = random.randint(lower, upper)

guess = int(input('pick a number between {low} and {up}:\n'.format(up=upper, low=lower)))
while guess > upper or guess < lower:
    print('Error: out of bounds!')
    guess = int(input('pick a number between {low} and {up}:\n'.format(up=upper, low=lower)))

while guess != randnum:
    if guess > randnum:
        guess = int(input('Too high! Try Again:\n'))
    if guess < randnum:
        guess = int(input('Too Low! Try Again:\n'))
else:
    print('Congratulations! You got it!')
