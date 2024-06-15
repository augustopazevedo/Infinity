primeiro_numero = int(input("Insira primeiro número " ))
segundo_numero = int(input("Insira segundo número "))
terceiro_numero = int(input("Insira terceiro número ")) 

if primeiro_numero > segundo_numero and segundo_numero >= terceiro_numero:
    print (f"O número maior é {primeiro_numero} O menor é {terceiro_numero}")

elif segundo_numero > primeiro_numero and primeiro_numero >= terceiro_numero:
    print (f"O número maior é {segundo_numero} O menor é {terceiro_numero}")

elif terceiro_numero > segundo_numero and segundo_numero >= primeiro_numero:
    print(f"O número maior é {terceiro_numero} O menor é {primeiro_numero}")

elif terceiro_numero > primeiro_numero and primeiro_numero >= segundo_numero:
    print (f"O número maior é {terceiro_numero} O menor é { segundo_numero}")
else:
    print(f"O número maior é {primeiro_numero} O menor é {segundo_numero}")
    




