estoque = {"tomate": [1000, 2.30],
"alface": [500, 0.45],
"batata": [2000, 1.20],
"feijão": [100, 1.50]}

print("Nós temos os seguintes produtos: ")
for nome,produto in estoque.items():
    print(f"nome: {nome} quantidade: {produto[0]} preço: {produto[1]}")

nomeProduto = input("Qual produto você quer comprar?\n")
for i in range(len(estoque)):
    for nomeProd,produto in estoque.items():
        if nomeProduto == nomeProd:
            qntCompra = int(input("Quantos você quer comprar?\n"))
            soma = qntCompra * produto[1]
            if produto[0] < qntCompra:
                print("Não pode comprar mais do que tem no estoque!")
            else:
                produto[0] -= qntCompra
                print(f"Você comprou {qntCompra} de {nomeProd}\nSaiu por {soma} e sobrou no estoque {produto[0]} ")
                exit()