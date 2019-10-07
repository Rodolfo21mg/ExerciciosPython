Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura Sequencial"""

tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de conexao (em Mbps): '))
tamanhoBits = tamanho * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print 'Tempo aproximado de download:', tempoMinutos, 'minutos'