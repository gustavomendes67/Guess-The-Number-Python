import random

quantidade = int(input("Digite a quantidade máxima de números que você deseja jogar: "))
print("Você escolheu o número ", quantidade, "como limite.")

numero_secreto = random.randint(1, quantidade)

tentativas = 0

while True:
    numero = int(input(f"Escolha um número de 1 a {quantidade}: "))

    tentativas += 1

    if numero == numero_secreto:
        print("Você acertou usando", tentativas, "tentativas.")
        break
    elif numero > numero_secreto:
        print("Digite um número menor!")
    else:
        print("Digite um número maior!")