def calcular_imc(peso, altura):
    ## Calcula el índice de masa corporal (IMC) dado el peso y la altura.
    imc = peso / altura
    return imc
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
print(f"su indice de masa corporal es: {calcular_imc(peso, altura),}")