import random

numero_secreto = 7
chute = int (input("escolha um numero de 1 a 10: "))
print(f"Voce escolheu o numero: {chute}")

if chute == numero_secreto:
        print("Voce acertou Parabens!!!")
elif chute > numero_secreto:
        print("Voce errou, Tente um numero menor")
else:
        print("Voce errou, Tente um numero maior")