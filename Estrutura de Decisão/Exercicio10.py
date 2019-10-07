Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """Una – Barreiro
Rodolfo Joarlei de Oliveira – RA 318118181
Algoritmos e Estrutura de Dados – Alexandre Oliveira 
Resposta Lista de Exercícios 
Estrutura de Decisão"""

print 'Informe o turno em que voce estuda'
print '[M]atutino'
print '[V]espertino'
print '[N]oturno'
turno = input('Opcao escolhida: ').upper()

if (turno == 'M'):
    print 'Bom dia!'
elif (turno == 'V'):
    print 'Boa tarde!'
elif (turno == 'N'):
    print 'Boa noite!'
else:
    print 'Valor invalido'
