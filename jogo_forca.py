#Jogo da forca
print('Bem vindo  a jogo da forca vc tem 10  tantativa para acretar  a palavra secreta ')
#palavra secreta
palavras_secretas=['P','Y','T','H','O','N']
palavra = []
#contador de error
erro = 0
while erro < 10:
    #digitando a letra para ver se ta certa ou errada
    letra = input('Digite uma letra: ').upper()
    if letra in palavra:
        print(f'vc ja digitou a letra {letra} tente outra letra')
        continue
    palavra.append(letra)

    if letra in palavras_secretas:
        print(f'Parabens vc acertou a letra {letra} esta na palavra secreta')
   
    else:
            erro += 1
            print(f'Errou! a letra {letra} não esta na palavra secreta')


 #for loop para mostrar a palavra secreta com as letras acertadas e as letras erradas
    for letra in palavras_secretas:
        if letra in palavra:
            print(letra, end=' ')
        else:
            print('_', end=' ')
#finalmente mostra quantas tentativas o jogador tem e se ele ganhou ou perdeu o jogo
    print(f' \n vc tem {10 - erro} tentativas')
    print('\n-----------------------------------\n')
    if len(palavra) == len(palavras_secretas):
        print('Parabens vc ganhou o jogo da forca')
        break
    elif erro == 10:
        print('Acabaram as tentativas! vc perdeu o jogo da forca')
   
print('A palavra secreta era: ', palavras_secretas)