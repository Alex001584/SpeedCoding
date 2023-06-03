import random
import os
os.system("clear")

Rondas = 3
Score = [0,0]
for i in range(Rondas):
    print("\n\t--- RONDA "+str(i+1)+" ---")
    Dados = [(random.randint(1, 6), random.randint(1, 6)),(random.randint(1, 6), random.randint(1, 6))]
    Sumas = [(Dados[0][0]+Dados[0][1]),(Dados[1][0]+Dados[1][1])]

    print("Tirada del P1: {} y {} = {}".format(Dados[0][0],Dados[0][1],(Dados[0][0]+Dados[0][1])))
    print("Tirada del P2: {} y {} = {}".format(Dados[1][0],Dados[1][1],(Dados[1][0]+Dados[1][1])))
    Ganador = max((Dados[0][0]+Dados[0][1]), (Dados[1][0]+Dados[1][1]))


    if Sumas[0] == Sumas[1]:
        print("Empate con "+str(Sumas[0]))
    elif Ganador == Sumas[0]:
        print("El ganador es P1 con "+str(Sumas[0])+" +100")
        Score[0]+=100
    else:
        print("El ganador es P2 con "+str(Sumas[1])+" +100")
        Score[1]+=100

print("\nSCORE\n P1: {}\t P2: {}".format(Score[0],Score[1]))

input()
os.system("clear")