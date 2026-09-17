#Adivinha o numero que eu to pensando!
import random as rd
numero=rd.randint(1,100)
tentativas=4
while tentativas >0:
    tentativas -=1
    print(f'3 Tentativa : Faltam {tentativas} ')
    chute= int(input('Digite um numero de 1 a 10: '))
    if chute == numero:
        print(f'Parabens vc ganhou! {numero} o numero  que eu estava pensando :)')
        break
    elif chute < numero:
        print("O você chutou o numero menor que o seu numero!")
    elif chute > numero:
        print("O você chutou o numero maior que o seu numero!")
    else:
        print('Errou! tente de novo!')
print(f'Acabaram as tentativas! O numero que eu estava pensando era {numero} :(')