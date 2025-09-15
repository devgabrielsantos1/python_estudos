
pessoas = {"Gabriel" : {"Nome":"Gabriel", "Idade":21,"Cidade":"Itaquaquecetuba"},
          "Julia":{"Nome":"Júlia", "Idade":22,"Cidade":"Itaquaquecetuba"},
          "Bruno":{"Nome":"Bruno", "Idade":33,"Cidade":"Itaquaquecetuba"}
}

for pessoa in pessoas:
    nome_pessoa = pessoas[pessoa]["Nome"]
    idade_pessoa = pessoas[pessoa]["Idade"]
    cidade_pessoa = pessoas[pessoa]["Cidade"]

    print(f"{nome_pessoa.ljust(10)}| {idade_pessoa}| {cidade_pessoa}")


pessoas["Gabriel"]["Idade"] = 25 

print(pessoas["Gabriel"])

pessoas["Gabriel"]["Profissão"] = "Programador"

print(pessoas["Gabriel"])

del pessoas["Bruno"]["Cidade"]
print(pessoas["Bruno"])




frase = input("Digite uma frase: ")


palavras = frase.split()


frequencia = {}


for palavra in palavras:
    palavra = palavra.lower()  
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Frequência das palavras:")
for palavra, qtd in frequencia.items():
    print(f"{palavra}: {qtd}")
