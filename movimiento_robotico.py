def movimiento_robot(orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str) -> str:
    if orientacion_actual == "N":
        p = 0
    elif orientacion_actual == "E":
        p = 1
    elif orientacion_actual == "S":
        p = 2
    elif orientacion_actual == "W":
        p = 3

    if giro_1 == "L":
        p = p - 1
    elif giro_1 == "R":
        p = p + 1
    elif giro_1 == "H":
        p = p + 2
    elif giro_1 == ".":
        p = p
    
    if giro_2 == "L":
        p = p - 1
    elif giro_2 == "R":
        p = p + 1
    elif giro_2 == "H":
        p = p + 2
    elif giro_2 == ".":
        p = p

    if giro_3 == "L":
        p = p - 1
    elif giro_3 == "R":
        p = p + 1
    elif giro_3 == "H":
        p = p + 2
    elif giro_3 == ".":
        p = p

    if p == 0 or p % 4 == 0:
        return "N"
    elif p == 1 or p % 4 == 1:
        return "E"
    elif p == 2 or p % 4 == 2:
        return "S"
    elif p == 3 or p % 4 == 3:
        return "W"

print(movimiento_robot("N","H","H","R"))