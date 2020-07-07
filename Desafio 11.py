import random
import string
chars = string.ascii_letters + string.digits
print("Escolha quantos caracteres tera a senha:")
size = int(input())

senha = ''.join(random.choice(chars) for _ in range(size))
print(senha)