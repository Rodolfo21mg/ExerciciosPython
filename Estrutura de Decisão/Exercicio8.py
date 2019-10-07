Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura de Decisão"""

preco1 = int(input('Informe o primeiro preco: '))
preco2 = int(input('Informe o segundo preco: '))
preco3 = int(input('Informe o terceiro preco: '))

if (preco1 == preco2) and (preco1 == preco3):
    print 'Pode comprar qualquer um, ja que os precos sao iguais.'
elif (num1 < num2) and (num1 < num3):
    print 'Compre pelo primeiro preco'
elif (num2 < num3):
    print 'Compre pelo segundo preco'
else:
    print 'Compre pelo terceiro preco'
