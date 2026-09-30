s = "senai123"

r = str(input("digite a senha: "))

while s != r:
    print("acesso negado")
    r = str(input("tente novamente: "))

print("acesso liberado")