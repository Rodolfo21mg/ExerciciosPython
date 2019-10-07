Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura Sequencial"""

a = float(input("Quanto você ganha por hora:"))
b = int(input("Horas trabalhadas:"))

salariobruto = a * b

ir = (salariobruto*0.11)
inss = (salariobruto*0.08)
sindicato = (salariobruto*0.05)

salarioliquido = (salariobruto - ir - inss - sindicato)

print ("+ Salário Bruto: R$", salariobruto)
print ("- IR (11%): R$" , ir)
print (" - INSS (8%): R$" , inss)
print (" - Sindicato (5%): R$" , sindicato)
print (" + Salário Liquido : R$" , salarioliquido)
