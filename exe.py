numero = int(input("Digite um número para descobrir se par ou impar: \n"))

resultado = numero %2

if resultado == 0 :
    print("Você digitou um número par")

else:
    print("Você digitou um número impar")