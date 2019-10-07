Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura Sequencial"""

tamanho = float(input('Quantos metros quadrados devem ser pintados: '))
litros = tamanho / 3.0
latas = int(litros / 18.0)
if (litros % 18 != 0):
    latas += 1

print 'Voce devera comprar', latas, 'latas.'
print 'O valor total eh:', latas * 80

