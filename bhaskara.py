#ax²+bx+c=0
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
#delta = b²-4ac
delta = b**2 - 4*a*c
print('O valor de delta é: ', delta)
#x = (-b +- raiz(delta)/2a)
x1 = (-b - delta**0.5) / 2*a
x2 = (-b + delta**0.5) / 2*a
print('O valor de x1 é: ',x1)
print('O valor de x2 é: ',x2)
