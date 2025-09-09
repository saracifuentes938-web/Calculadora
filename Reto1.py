Hemog = float(input("Digite su hemoglobina en g/dl: "))
Genero = int (input("Digite su genero, 1=Hombre,2= Mujer: "))

if Genero == 1:
    if Hemog < 12.2:
        print("Su hemogloina es baja")
    elif Hemog >= 12.2 and Hemog <= 16.6:
        print("Su hemoglobina es normal")
    else: 
        print ("Su hemoglobina es alta")
elif Genero == 2:
    if Hemog < 12.6:
        print ("Su hemoglobina es baja")
    elif Hemog >= 12.6 and Hemog <= 15:
        print ("Su hemoglobina es normal")
    else: 
        print ("Su hemoglobina es alta")
else: 
    print("No es posible generar la alerta")

