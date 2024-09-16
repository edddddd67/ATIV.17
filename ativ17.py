# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.
n=int(input("digite seu ano:"))

if n % 100 !=0 and n % 4 == 0 or n % 400 == 0:
    print("ano bissexto")

else:
    print("ano não bissexto")
