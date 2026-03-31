#algoritmo mudanca_de_preco

#declaração de variável
preco_atual: float = 0
media_mensal: float = 0

def comparacao(preco_a , media_m):
    if media_m < 500 and preco_a < 30:
        preco_novo = preco_a * 1.10

    elif media_m >= 500 and media_m < 1000 and preco_a >= 30 and preco_a < 80:
        preco_novo = preco_a *1.15

    elif media_m > 1000 and preco_a > 80:
        preco_novo = preco_a *0.95

    else:
        preco_novo = preco_a
        print("O preço não mudou.")

    print("O novo preço do produto é R$" , preco_novo)

def main():
    global preco_atual
    global media_mensal

    preco_atual = float(input("Digite o preço atual do produto: "))
    media_mensal = float(input("Digite a média mensal do produto: "))

    comparacao(preco_atual , media_mensal)

if (__name__ == '__main__'):
    main()