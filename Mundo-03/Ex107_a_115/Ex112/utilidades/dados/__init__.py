def leiadado(valor=''):
    verificar = False
    while verificar == False:
        valor = (input("Digite o valor: ")).replace(",",".")

        if valor.isalpha():
            print('\033[31mERRO! Valor não informado corretamente\033[m')
        else:
            verificar = True
            return float(valor)

