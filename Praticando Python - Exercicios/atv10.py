# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

renda_mensal = float(input("Digite a sua renda mensal: "))
valor_parcela = int(input("Quantas parcelas deseja: "))



negado = renda_mensal * 0.3

if valor_parcela >= negado:
    print("Empréstimo negado, valor da parcela acima dos 30% da renda")
else:
    print(f"Empréstimo aprovado, valor das parcelas: R$ {valor_parcela}")