from datetime import date
 
def calcular_edad(fecha_nac):
    hoy = date.today()
    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    return edad


fecha_nac = date(1990, 5, 23)
edad = calcular_edad(fecha_nac)

print(edad)
