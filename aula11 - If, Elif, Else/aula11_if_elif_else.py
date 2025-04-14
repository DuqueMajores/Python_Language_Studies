# Sistema de Recomendação de Atividades

def condition(clima: str, horario: str, felling: str):
    if(clima == "ensolarado"):
        if(horario == "manha"):
            if(felling == "animado"):
                print("Recomendo uma caminhada no parque")
            elif(felling == "cansado"):
                print("Recomendo relaxar ao ar livre")
            else:
                print("Não entendi como se sente...")
        elif(horario == "tarde"):
            if(felling == "animado"):
                print("Recomendo um piquinique")
            elif(felling == "cansado"):
                print("Recomendo jogar futebol")
            else:
                print("Não entendi como se sente...")
        elif(horario == "noite"):
            if(felling == "animado"):
                print("Recomendo olhar as estrelas")
            elif(felling == "cansado"):
                print("Recomendo dormir mais cedo")
            else:
                print("Não entendi como se sente...")
        else:
            print("Digite o horario correto...")
    elif(clima == "chuvoso"):
        if(horario == "manha"):
            if(felling == "animado"):
                print("Recomendo ler um livro")
            elif(felling == "cansado"):
                print("Recomendo assistir um filme")
            else:
                print("Não entendi como se sente...")
        elif(horario == "tarde"):
            if(felling == "animado"):
                print("Recomendo cozinhar algo novo")
            elif(felling == "cansado"):
                print("Recomendo tirar uma soneca")
            else:
                print("Não entendi como se sente...")
        elif(horario == "noite"):
            if(felling == "animado"):
                print("Recomendo ouvir musica")
            elif(felling == "cansado"):
                print("Recomendo assistir uma série")
            else:
                print("Não entendi como se sente...")
        else:
            print("Digite o horario correto...")
    elif(clima == "frio"):
        if(horario == "manha"):
            if(felling == "animado"):
                print("Recomendo tomar uma bebida quente")
            elif(felling == "cansado"):
                print("Recomendo dormir mais um pouquinho")
            else:
                print("Não entendi como se sente...")
        elif(horario == "tarde"):
            if(felling == "animado"):
                print("Recomendo fazer exercicios")
            elif(felling == "cansado"):
                print("Recomendo jogar video game")
            else:
                print("Não entendi como se sente...")
        elif(horario == "noite"):
            if(felling == "animado"):
                print("Recomendo sair com a namorada")
            elif(felling == "cansado"):
                print("Recomendo dormir com a namorada")
            else:
                print("Não entendi como se sente...")
        else:
            print("Digite o horario correto...")
    elif(clima == "nublado"):
        if(horario == "manha"):
            if(felling == "animado"):
                print("Recomendo organizar a casa")
            elif(felling == "cansado"):
                print("Recomendo estudar um pouco")
            else:
                print("Não entendi como se sente...")
        elif(horario == "tarde"):
            if(felling == "animado"):
                print("Recomendo visitar algum amigo")
            elif(felling == "cansado"):
                print("Recomendo aprender algo novo online")
            else:
                print("Não entendi como se sente...")
        elif(horario == "noite"):
            if(felling == "animado"):
                print("Recomendo pedir uma pizza")
            elif(felling == "cansado"):
                print("Recomendo meditar")
            else:
                print("Não entendi como se sente...")
        else:
            print("Digite o horario correto...")
    else:
        print("Não captei o clima...")

clima = str(input("Qual é o clima? [ensolarado / chuvoso / frio / nublado]: "))
horario = str(input("Qual é o horário do dia? [manha / tarde / noite]: "))
felling = str(input("Como você está se sentindo? [animado / cansado]: "))

condition(clima.lower(), horario.lower(), felling.lower())

