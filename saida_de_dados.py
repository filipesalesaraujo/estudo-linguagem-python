print("bom dia", end="")
print("boa noite", end="")

print("bom dia")
print("boa noite")

x1: int
y1: int
x1 = 10
y1 = 20
print(x1)
print(y1)

x2: float
x2 = 2.3456
print("{:.2f}".format(x2))

idade: int
salario: float
nome: str
sexo: str
idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"
print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))