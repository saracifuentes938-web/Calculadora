HB= HN= HA= MB= MN= MA= 0
CantP = int(input("Digite la cantidad de pacientes: "))
for i in range(CantP):
    Hemog = float(input("Digite la cantidad de henoglobina en g/dL: "))
    Genero = int(input("Digite su genero 1=Hombre, 2=Mujer: "))
    if Genero == 1:
        if Hemog < 12.2:
            HB += 1
        elif Hemog >= 12.2 and Hemog <= 16.6:
            HN += 1
        else:
            HA += 1
    elif Genero == 2:
        if Hemog < 12.6:
            MB += 1
        elif Hemog >= 12.6 and Hemog <= 15:
            MN += 1
        else:
            MA += 1
    else:
        print("No es posible generar la alerta")
print(f"Total procesados: {HB , HA , HN , MB , MA , MN}")