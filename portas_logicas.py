idade = float(input ("Qual a sua idade?"))
convite = input("Você tem convite? (S/N)")

if (idade >= 18 and convite == "S"):
	entrada = True
	print("Seja bem vindo à boate Infinity")
else:
	entrada = False
	print ("Deu Ruim")