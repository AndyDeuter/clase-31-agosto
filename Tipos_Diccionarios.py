Datos_Basicos = {"Nombres": "Juan Carlos",
                 "Apellidos":"Perez Garcia",
                 "DUI":"0125487-9",
                 "Fecha_Nacimiento":"23/07/1980",
                 "Lugar_Nacimiento":"Salvadoreña",
                 "Estado_civil":"Complicado"
                 }


print("\nDetalle de Diccionario")
print("===========================")

print("\nClaves del diccionario: ", Datos_Basicos.keys())
print("\nValores del diccionario: ", Datos_Basicos.values())
print("\nElementos del diccionario: ", Datos_Basicos.items())

print("\nInscripción del curso")

print("\nDatos del participante")
print("DUI:", Datos_Basicos["DUI"])
print("Nombre Completo:", Datos_Basicos["Nombres"], Datos_Basicos["Apellidos"])
