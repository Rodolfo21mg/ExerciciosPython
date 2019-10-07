Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura Sequencial"""

tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = (tamanho / 6.0) * 1.1  # 10% de folga
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

if (litros % 18 != 0):
    latas += 1

if (litros % 3.6 != 0):
    galoes += 1

mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print 'Latas:', latas, '. Valor:', latas * 80
print 'Galoes:', galoes, '. Valor:', galoes * 25
print 'Latas:', mixLatas, 'e', mixGaloes, '. Valor: ', \
    (mixLatas * 80)+(mixGaloes*25)
