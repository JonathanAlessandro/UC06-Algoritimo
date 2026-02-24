notas=[]
total=0
for i in range(4):
    notas_aluno = int(input("Digite um numero: "))
    notas.append(notas_aluno)
    total+=notas_aluno

print(f"{sum(notas)/4}")
print(f"A media foi {total/4}")


# for n in notas:
#     total+=n
print(total)
