'''3. Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:

a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:'''


salario_hora  = float(input("Quanto voce ganah por hora?"))
horas_trabalhadas =  int(input("Quantas horas voce trabalha no mes?"))

salario_brunto =salario_hora*horas_trabalhadas

imposto = salario_brunto* 0.11
inss = salario_brunto*0.08
sindicato = salario_brunto*0.05
salario_liquido =salario_brunto - imposto - inss - sindicato

print(f"Salario Bruto: R${salario_brunto}")
print(f"Imposto de Renda: R${imposto}")
print(f"INSS: R${inss}")
print(f"Sindicato: R${sindicato}")
print(f"Descontos: R${imposto+inss+sindicato}")
print(f"Salario Liquido: R${salario_liquido}")


