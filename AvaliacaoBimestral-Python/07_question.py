nome = input("Nome do Aluno: ")
disciplina = input("Disciplina: ")
nota1 = float(input(f"Nota da parcial de {disciplina}: "))
nota2 = float(input(f"Nota da bimestral de {disciplina}: "))
media = (nota1 + nota2)/2
print(f"A media de {nome} é {media}.")
if media >= 6:
    situacao = "aprovado"
    print(f"{nome} está {situacao} na {disciplina}.")
else:
    situacao = "reprovado"
    print(f"{nome} está {situacao} na {disciplina}.")