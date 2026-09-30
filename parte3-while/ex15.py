p = 0
n = 0

while True:
    n = int(input("digite um número (0 para parar): "))

    if n == 0:
        break

    elif n<0:
        n=n+1

    else:
        p=p+1

print("positivos: ", p, "\nnegativos: ", n)