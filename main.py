from time import sleep

print("Faça o seu voto consciente!")

jair = 22
olivio = 17
branco = 999
nulo = 0

while True:
    # pergunta ao usuario qual candidato ele irá votar
    user = int(input("Digite o numero do seu candidato: "))
    if user == 22:
        jair += 1
    elif user == 17:
        olivio += 1
    elif user == 999:
        branco += 1
    elif user == 0:
        nulo += 1
    else:
        print("Candidato não conhecido!")
        break
    computer = str(input("Quer continuar?[S/N] ")).upper()
    if computer == 'N':
        if computer not in 'N' or computer not in 'S':
            print("Não entendi sua resposta!")
            break
    else:
        print("Loading...")
        sleep(2)
