# Gerador de senha 
import random as rd
import getpass as gt

def gerar_senha(tamanho):
    caract = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+" 

    senha = ""
    for i in range(tamanho):
        senha += rd.choice(caract)
    return senha 
    
#vc vai quer criar uma senha ou ser aleatrória?
print("Gerador de senha")
login = input("Digite seu login:")
criar = input("Quer criar uma senha ou que seja aleatória? (S/N):").upper()

if criar == "S":
    senha = gt.getpass("Digite a sua senha: ")
    print("\n Login: ", login)
    print (" Senha: ", senha)
elif criar == "N":
    aleatoria = int(input("Digite o tamanho da senha aleatróia:"))
    senha = gerar_senha(tamanho=aleatoria)
    print("\n Login: ", login)
    print (" Senha: ", senha) 
else:
    print("Opcão de falha: tente de novo!")

