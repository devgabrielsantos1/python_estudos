#Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperarura_atual = int(input("Digite a temperatura atual: "))

if temperarura_atual > 25 :
    print("Temperatura acima do limite permitido!")
else:
    print("Temperatura dentro do limite")