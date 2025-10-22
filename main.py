salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador júnior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("diretor")