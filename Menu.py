def suma(N1, N2):
    operacion = N1 + N2
    return "La suma de los dos numeros es: " + str(operacion)

def multiplicacion (N1, N2):
    operacion = N1 * N2
    return "El resutado de la multiplicacion es: " + str(operacion)

def Potencia (N1, N2):
    operacion = N1 ** N2
    return "El resultado de la potenciacion es: " + str(operacion)

def raiz (N1, N2):
    operacion = N1 ** (1.0 / N2)
    return "El resultado de la raiz es: " + str(operacion)

print("Menu de calculadora")
print("1=Suma 2=Resta 3=Multiplicacion 4=Division 5=Exponente 6=Raiz cuadrada " )

ope = int (input("Digite el numero de la operacion: "))

Num1 = float(input("Digite primer numero: "))
Num2 = float(input("Digite segundo numero: "))

if 1 == ope:
    sumafinal= suma(Num1, Num2)
    print(sumafinal)
elif 3 == ope: 
    multiplicacionfinal = multiplicacion (Num1, Num2)
    print(multiplicacionfinal)
elif 5 == ope:
    Potenciafinal = Potencia (Num1, Num2)
    print(Potenciafinal)
elif 6 == ope:
    raizfinal = raiz(Num1, Num2)
    print(raizfinal)