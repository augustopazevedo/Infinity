numero_alvo =  55
numero_de_tentativas = 5
chute_usuario = int(input("Dê um palpite entre 1 e 100: "))

while (chute_usuario != numero_alvo):
    numero_de_tentativas -= 1
    if numero_de_tentativas == 0:
        break
    if chute_usuario < numero_alvo:
        print ("O Valor Está Menor")
    else:
        print("O Valor Está Acima")
    chute_usuario = int(input("Dê um palpite entre 1 e 100: "))

else:
    print("Acertou!")

print ("Fim de Jogo!")
    


