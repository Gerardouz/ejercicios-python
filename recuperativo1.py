arreglo = [4,"+",15,"*",2,"-",6]
menor = arreglo[0] * arreglo[2] * arreglo[4] * arreglo[6] + 100000
mayor = 0

PrimerOperando = True
for elem in arreglo:
    if (type(elem) == int):
        if (PrimerOperando == True):
            Operando1 = elem
            PrimerOperando = False
        else:
            Operando2 = elem
            if (Op == "+"):
                Resultado = Operando1 + Operando2
                if Resultado > mayor:
                  mayor = Resultado
                if Resultado < menor:
                  menor = Resultado
                
            if (Op == "-"):
                Resultado = Operando1 - Operando2
                if (Resultado > mayor):
                  mayor = Resultado
                if (Resultado < menor):
                  menor = Resultado
                
            if (Op == "*"):
                Resultado = Operando1 * Operando2
                if (Resultado > mayor):
                  mayor = Resultado
                if (Resultado < menor):
                  menor = Resultado
            if (Op == "/"):
                Resultado = Operando1 / Operando2
                if (Resultado > mayor):
                  mayor = Resultado
                if (Resultado < menor):
                  menor = Resultado
                
            Operando1 = Resultado
    else:
        Op = elem

print (Resultado)
print ("el resultado parcial mayor es ", mayor)
print ("el resultado parcial menor es ", menor)