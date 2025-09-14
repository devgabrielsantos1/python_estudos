# Exercicio 01

# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print(f"{numero} é um número par")
# else:
#     print(f"{numero} é um número impar")


# Exercicio 02

# idade = int(input("Digite a sua idade: "))

# if idade >= 0 and idade <= 12:
#     print("Criança")
# elif idade > 12 and idade < 19:
#     print("Adolescente")
# else:
#     print("Maior de idade")


# exercicio 03

# usuario_correto = "gb4402"
# password_correta = "gebe123"

# usuario = input("Digite o usuario: ")
# password = input("Digite a senha: ")

# if usuario == usuario_correto and password == password_correta:
#     print("Login efetuado com sucesso!")
# elif usuario == usuario_correto and password != password_correta:
#     print("Senha incorreta!")
# elif usuario != usuario_correto and password == password_correta:
#     print("Usuario incorreto!")
# else:
#     print("Usuario e senha incorreto!")


x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x > 0 and y > 0:
    print("Primeiro Quadrante")
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif(x < 0 and y < 0):
    print("Terceiro Quadrante")
elif(x > 0 and y < 0):
    print("Quarto Quadrante")
else: 
    print("Eixo de origem")