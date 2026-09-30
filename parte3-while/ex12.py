soma = 0

while True:
    n = int(input("digite um número (0 para parar): "))

    if n == 0:
        break

    soma = soma + n

print("soma:", soma)