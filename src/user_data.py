# Simulador de nomina

lista_usuarios = [
    {
        "Nombre" : "Felipe",
        "Apellido" : "Sanchez",
        "Edad" : 27,
        "Salario" : 1750905,
        "Auxilio de transporte" : False,
        "Contrato" : "Termino indefinido",
        "Horas extras" : 0,
        "Remoto" : False
    },

    {
        "Nombre": "Elena",
        "Apellido": " Garcia",
        "Edad": 35,
        "Salario": 1750905,
        "Auxilio de transporte": True,
        "Contrato": "Termino fijo",
        "Horas extras": 12,
        "Remoto": True

    },

    {
        "Nombre": "Isac",
        "Apellido": "Arrieta",
        "Edad": 22,
        "Salario": 1750905,
        "Auxilio de transporte": False,
        "Contrato": "Aprendizaje",
        "Horas extras": 0,
        "Remoto": True
    },
    
    {
        "Nombre": "Fernanda",
        "Apellido": "Aristizabal",
        "Edad": 31,
        "Salario": 2500000,
        "Auxilio de transporte": True,
        "Contrato": "Obra labor",
        "Horas extras": 6,
        "Remoto": False
    },

    {
        "Nombre": "Raúl",
        "Apellido": "Mendez",
        "Edad": 41,
        "Salario": 3500000,
        "Auxilio de transporte": False,
        "Contrato": "Prestación de servicios",
        "Horas extras": 0,
        "Remoto": False
    }

]

print(lista_usuarios)
print(type(lista_usuarios))
print(lista_usuarios[0])
print(len(lista_usuarios))
print(lista_usuarios[0]["Nombre"])

nuevos_usuarios = {}

nuevos_usuarios["Nombre"] = input("Ingrese el nombre del nuevo usuario: ")
nuevos_usuarios["Apellido"] = input("Ingrese el apellido del nuevo usuario: ")  
nuevos_usuarios["Edad"] = int(input("Ingrese la edad del nuevo usuario: "))
nuevos_usuarios["Salario"] = int(input("Ingrese el salario del nuevo usuario: "))
nuevos_usuarios["Auxilio de transporte"] = input("¿El nuevo usuario recibe auxilio de transporte? (True/False): ") == "True"
nuevos_usuarios["Contrato"] = input("Ingrese el tipo de contrato del nuevo usuario: ")
nuevos_usuarios["Horas extras"] = int(input("Ingrese las horas extras del nuevo usuario: "))
nuevos_usuarios["Remoto"] = input("¿El nuevo usuario trabaja de forma remota? (True/False): ") == "True"

print(nuevos_usuarios)
print(type(nuevos_usuarios["Remoto"]))
nuevos_usuarios["Nombre"]= nuevos_usuarios["Nombre"].capitalize()
print (nuevos_usuarios)
lista_usuarios.append(nuevos_usuarios)
print(lista_usuarios)
print(len(lista_usuarios))