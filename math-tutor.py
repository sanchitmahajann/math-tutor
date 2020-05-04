import random
import math

print('Welcome to Math Tutor 1.0')
print('*************************')

num_rounds = int(input('How many questions do you want? '))
for n in range(num_rounds):
	numbers = [i for i in range(11, 31)]
	question = random.sample(numbers, 2)
	product = math.prod(question)

	answer = int(input(f'Enter the product of {question[0]} and {question[1]}: '))
	
	if answer == product:
		print('Correct!')
	else:
		print('Wrong Answer!')

print('GG!')