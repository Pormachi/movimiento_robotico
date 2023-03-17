def picas_y_fijas(numero_secreto:int, intento:int)->dict:
    """ Esta función consiste en un pequeño juego que consiste en adivinar
    un número (número_secreto) en la menor cantidad de intentos y nos devolverá
     un diccionario """

    diccionario = {}
    diccionario["FIJAS"] = 0
    diccionario["PICAS"] = 0
    
    if str(intento//1000) in str(numero_secreto):
        if numero_secreto//1000 == intento//1000:
            diccionario["FIJAS"] += 1
        else:
            diccionario["PICAS"] += 1
    if str((intento%1000)//100) in str(numero_secreto):
        if (numero_secreto%1000)//100 == (intento%1000)//100:
            diccionario["FIJAS"] += 1
        else:
            diccionario["PICAS"] += 1
    if str(((intento%1000)%100)//10) in str(numero_secreto):
        if ((numero_secreto%1000)%100)//10 == ((intento%1000)%100)//10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["PICAS"] += 1 
    if str(((intento%1000)%100)%10) in str(numero_secreto):
        if ((numero_secreto%1000)%100)%10 == ((intento%1000)%100)%10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["PICAS"] += 1 
    
    return diccionario