verdad = 0
while verdad == 0:
    usr = int(input("pon el valor de la invercion : "))
    print("el capital ganado por mes es : ", int((usr * 2) / 100))
    ver = input("deseas salir ? si/no . ")
    if ver == "si":
        verdad = 1
        # 1.Suponga que un individuo desea
        # invertir su capital en un banco y desea saber
        # cuánto dinero ganará después de un mes si el
        # banco paga a razón de 2% mensual
