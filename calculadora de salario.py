# Pergunte ao usuário o salário/hora e a quantidade de horas
salario_hora = float( input("Informe o valor da sua hora de trabalho"))
horas_totais = float( input("Informe quantas horas trabalhadas no mês"))
# Calcule o salário bruto 
salario_bruto = salario_hora * horas_totais
print (salario_bruto)
# Calcule os impostos
# 11% imposto de renda, 8% INSS, 5% Sindicato
if salario_bruto >= 5000.0:
	imposto_ir = salario_bruto * 0.11
elif salario_bruto >= 2000.0:
	imposto_ir = salario_bruto * 0.08
else:
	imposto_ir = 0	
imposto_inss = salario_bruto * 0.08 
imposto_sindicato = salario_bruto* 0.05
# Calcule o salário líquido
salario_liquido = salario_bruto - imposto_ir - imposto_inss - imposto_sindicato
# Mostrar os resultados
print (f"Salário bruto: R${salario_bruto}")
print (f"INSS (8%): R$ {imposto_inss}")
print (f"IR (11%): R$ {imposto_ir}")
print (f"Sindicato (5%): R$ {imposto_sindicato}")
print (f"Salario Líquido: R$ {salario_liquido}")