a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("Digite o número da operação: ")

if op == "1":
    print("Resultado:", a + b)
elif op == "2":
    print("Resultado:", a - b)
elif op == "3":
    print("Resultado:", a * b)
elif op == "4":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero!")
else:
    print("Operação inválida.")
