Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura de Decisão"""

salario = float(input('Informe o valor do salario do colaborador: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
novoSalario = salario + aumento

print 'Salario antes do reajuste:', salario
print 'Percentual de aumento:', percentual, '%'
print 'Valor do aumento:', aumento
print 'Novo Salario:', novoSalario


