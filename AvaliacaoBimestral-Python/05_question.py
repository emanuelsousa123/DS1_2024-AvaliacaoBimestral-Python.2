hora = int(input("Digite uma hora entre 0 e 23: "))
if (12 > hora):
    print("Este é um horário da manhã.")
elif (12 <= hora < 18):
    print("Este é um horário da tarde.")
elif (18<= hora <= 23):
    print("Este é um horário da noite.")