#1
perguntas = ["Telefonou para a vitmia? \n","Esteve no local do crime? \n","Mora perto da vitima? \n","Devia para a vitima? \n","Já trabalho com a vitmia? \n"]
resultado = 0
print("Responda com Sim ou Nao")

for i in range(len(perguntas)):
    resposta = input(f"{perguntas[i]}")
    if resposta.lower() == "nao" or resposta.lower() == "sim":
        if resposta.lower() == "sim":
            resultado += 1
    else:
        print("Resposta Invalida!")
        exit()

match(resultado):
    case 0:
        print("Inocente!")
    case 1:
        print("Inocente!")
    case 2:
        print("Suspeita!")
    case 3:
        print("Cumplice!")
    case 4:
        print("Cumplice!")
    case 5:
        print("Assassino!")
    case _:
        print("Erro no código")
