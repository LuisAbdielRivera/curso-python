def sigZodiacal(Mes,Dia):
    if (Mes == 3 and Dia >= 21) or (Mes == 4 and Dia <= 20):
        return "Aries"
    
    elif(Mes == 4 and Dia >= 21) or (Mes == 5 and Dia <= 21):
        return "Tauro"
    
    elif(Mes == 5 and Dia >= 22) or (Mes == 6 and Dia <= 21):
        return "Geminis"
    
    elif(Mes == 6 and Dia >= 22) or (Mes == 7 and Dia <= 23):
        return "Cancer"
    
    elif(Mes == 7 and Dia >= 24) or (Mes == 8 and Dia <= 23):
        return "Leo"
    
    elif(Mes == 9 and Dia >= 23) or (Mes == 10 and Dia <= 21):
        return "Escorplo"
    
    elif(Mes == 10 and Dia >= 22) or (Mes == 11 and Dia <= 21):
        return "Sagitario"
    
    elif(Mes == 11 and Dia >= 22) or (Mes == 12 and Dia <= 19):
        return "Capricornio"
    
    elif(Mes == 1 and Dia >= 20) or (Mes == 2 and Dia <= 18):
        return "Acuario"
    
    elif(Mes == 2 and Dia >= 19) or (Mes == 3 and Dia <= 20):
        return "Piscis"
    
Mes = int(input ("Mes de nacimiento: "))
Dia = int(input ("Dia de nacimiento: "))
print ("Tu signo Zodiacal es: " ,sigZodiacal(Mes,Dia))