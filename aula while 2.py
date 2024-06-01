dinheiro_augusto = 30
preco_do_relogio = 40

if dinheiro_augusto >= preco_do_relogio:
    print("Relógio Vendido!")
else: 
    while dinheiro_augusto < preco_do_relogio:
        preco_do_relogio -=2
        print(" O novo preço é ", preco_do_relogio)
    print("Relógio vendido por", preco_do_relogio, "reais")
