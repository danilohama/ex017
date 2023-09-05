# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente  de um triangulo retangulo, calcule e
# mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))

'''
primeira forma de fazer o codigo sem precisar baixar o modulo...
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))'''
