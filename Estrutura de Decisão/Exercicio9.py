﻿Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura de Decisão"""

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
num3 = int(input('Informe mais um numero: '))

if (num1 >= num2) and (num1 >= num3):
    print num1
    if (num2 >= num3):
        print num2
        print num3
    else:
        print num3
        print num2
elif (num2 >= num3):
    print num2
    if (num1 >= num3):
        print num1
        print num3
    else:
        print num3
        print num1
else:
    print num3
    if (num1 >= num2):
        print num1
        print num2
    else:
        print num2
        print num1
