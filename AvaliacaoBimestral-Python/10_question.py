num = int(input("digite um numero: "))
print("A tabuada desse número é: ")
for contador in range(1, 11):
    print(f"{num} x {contador} = {num*contador}")