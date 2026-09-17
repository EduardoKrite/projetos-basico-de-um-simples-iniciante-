#o computador adivinha o numero do usuario
import random as rd
print("O computador vai tentar adivinhar o numero que vc esta pensando!")
numero= int(input("Digite um numero de 1 a 20: "))
tentativas = 5
while tentativas > 0:
    tentativas -=1
    chuta = rd.randint(1,20)
    print(f"faltam {tentativas} ")
    if chuta == numero:
        print("Parabens vc ganhou o computador acertou o numero que vc escreveu:")

        break
    elif chuta < numero:
        print("O computador chutou o numero menor que o seu numero!")
    elif chuta > numero:
        print("O computador chutou o numero maior que o seu numero!")
    else:
        print("O computador errou! tente de novo!")
        print("Seu numero e esse :", numero)
        print("O computador chutou esse numero: ",chuta)

print(f'Acabaram as tentativas! O computador não conseguiu adivinhar o numero que vc escreveu :(')
