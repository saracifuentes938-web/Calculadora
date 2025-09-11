CanPacientes = int(input("Digite la cantidad de pacientes: "))
HemoglobinaH = [0] * CanPacientes
HemoglobinaM = [0] * CanPacientes
NumeroH= NumeroM= SumaHombre= SumaMujer = 0
for i in range(CanPacientes):
    Hemoglobina= float(input("Digite su hemoglobina en g/dL: "))
    Genero= int(input("Digite su genero 1= Hombre, 2= Mujer: "))
    if Genero == 1:
        HemoglobinaH[NumeroH] = Hemoglobina
        NumeroH += 1
        SumaHombre += Hemoglobina
    elif Genero == 2:
        HemoglobinaM[NumeroM] = Hemoglobina
        NumeroM += 1
        SumaMujer += Hemoglobina
    else:
        print("Digite un genero valido")
    
if NumeroH > 0:
    PromedioH = SumaHombre / NumeroH
else:
    PromedioH = 0

if NumeroM > 0:
    PromedioM = SumaMujer / NumeroM
else:
    PromedioM = 0

if PromedioH < 12.2:
    AlertaH = "Baja"
elif PromedioH >= 12.2 and PromedioH <= 16.6:
    AlertaH = "Normal"
else:
    AlertaH = "Alta"

if PromedioM < 12.6:
    AlertaM = "Baja"
elif PromedioM >= 12.6 and PromedioM <= 15:
    AlertaM = "Normal"
else:
    AlertaM = "Alta"

SuperiorH= IgualH= InferiorH = 0
for i in range(NumeroH):
    if HemoglobinaH[i] > PromedioH:
        SuperiorH += 1
    elif round(HemoglobinaH[i], 2) == round(PromedioH, 2):
        IgualH += 1
    else:
        InferiorH += 1

SuperiorM= IgualM= InferiorM = 0
for i in range(NumeroM):
    if HemoglobinaM[i] > PromedioM:
        SuperiorM += 1
    elif round(HemoglobinaM[i], 2) == round(PromedioM, 2):
        IgualM += 1
    else:
        InferiorM += 1

print(round(PromedioH, 2), AlertaH)
print(round(PromedioM, 2), AlertaM)
print(SuperiorH, SuperiorM)
print(InferiorH, InferiorM)
print(IgualH, IgualM)