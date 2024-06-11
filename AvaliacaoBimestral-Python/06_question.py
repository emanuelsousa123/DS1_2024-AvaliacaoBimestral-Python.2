nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
if (idade < 16):
      print(f'O cidadão "{nome}" não atingiu a idade necessária para tirar o título de eleitor.')
else:
    print(f'O cidadão "{nome}" está apto para tirar seu título de eleitor')