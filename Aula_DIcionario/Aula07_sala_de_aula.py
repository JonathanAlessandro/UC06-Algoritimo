usuario= {
    "nome":"",
    "idade":"",
    "cidade":""
}

# usuario["nome"] = input("Digite seu nome: ")
# usuario["idade"] = input("Qual a sua idade? ")
# usuario["cidade"] = input("Qual cidade você mora? ")

print(f"Olá {usuario['nome']}, você tem {usuario['idade']} e mora em {usuario['cidade']}")



aluno = {
    "nome":"",
    "notas":[]
}
# aluno["nome"] = input("Digite seu nome: ")

i=0
total = 0

while i<=4:
    
    aluno["notas"].append(float(input("Digite a nota: ")))
    i+=1

# while aluno["notas"]<=4:
#     nota_unica = aluno["notas"]
#     total += nota_unica

print(aluno)

for nota in aluno["notas"]:
    total += nota

print(total/5)