def agilidade(var):
    print(f'Essa variável contém "{var}" e seu tipo é {type(var)}.\n')
 
ano = 1999
nota = 0.83
filme = "Matrix"
red_pill = True

vars = [ano, nota, filme, red_pill]
for x in vars:
    agilidade(x)