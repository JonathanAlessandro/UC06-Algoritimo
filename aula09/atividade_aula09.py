notas= []

def calculo_nota():
    i=0
    while i <6:
        i+=1
        nota = int(input(f"Digite {i} a nota do aluno: "))
        notas.append(nota)

    total = sum(notas)/len(notas)
    return total

def aprovacao():
    if calculo_nota()>7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")        

aprovacao()