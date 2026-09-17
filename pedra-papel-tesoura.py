import random

opecao= ['pedra', 'papel', 'tesoura']

escolha = random.choice(opecao)

usuario = input(f"Escolha: {opecao}")
print(f"vc escolheu {usuario}")
print(f"e a maquina recebeu: {escolha}")
if escolha == usuario :
    print("empate")
elif escolha == 'pedra' and usuario == 'tesoura':
    print("você perdeu")
elif escolha == 'papel' and usuario == 'pedra':
    print("você perdeu")
elif escolha == 'tesoura' and usuario == 'papel':
    print("você perdeu")

else:
    print("você ganhou ")