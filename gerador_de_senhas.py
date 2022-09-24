from random import choice
import string


def password():

    tam = int(input("Quantos dígitos você quer na sua senha? "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # string.ascii_letters retorna todas as letras maiúsculas e minusculas
    # string.digits retorna os números
    # string.punctuation retorna caracteres

    senha_segura = ''

    for i in range(tam):
        senha_segura += choice(caracteres)

    print(f'A Senha (Segura) Gerada é: {senha_segura}')



password()
