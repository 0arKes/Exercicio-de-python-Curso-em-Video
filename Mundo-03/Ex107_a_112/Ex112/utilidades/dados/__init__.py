def leiadado(msg):
    verificar = False
    while verificar == False:
        valor = (input(msg)).replace(",",".").strip()

        if valor.isalpha() or valor == '':
            print('\033[31mERRO! Valor não informado corretamente\033[m')
        else:
            verificar = True
            return float(valor)

