#TIME TEMPORAL
import time
contagem = int(input("Digite os segundos: "))
#Uma contagem regressiva 
if contagem > 0:
    for i in range(contagem,0,-1):
        print(i)

        time.sleep(1)
print("terminou o time: ")
