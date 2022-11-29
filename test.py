import random
import string

letters=string.ascii_letters
rand_str = ''.join(random.choice(letters) for i in range(6))
print(rand_str)
new = f'_{rand_str}'
filename='test'+f'_{rand_str}'
print(filename)