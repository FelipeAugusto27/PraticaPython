'''
Resolva a questão: Fazer um programa que pergunte o valor da conta a ser paga no restaurante.
O programa deve apresentar como resposta o valor da conta com o acréscimo de 10% do garçom
'''

# Input
conta = float(input("Digite o valor da conta R$"))

# calculo
pagar = (conta * 0.1) + conta

# output
print("Deve se pagar R$", pagar)

