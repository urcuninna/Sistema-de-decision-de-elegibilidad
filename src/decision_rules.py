# uso de reglas de decisión

from user_data import lista_empleados

empleado = lista_empleados[0]

remote_work =(empleado["Remoto"] == "Si" and
              empleado["Permanencia"] >= 6 and
              empleado["Aprobación"] == "Si" and
              empleado["Registro disciplinario"] == "No")

print(remote_work)

performance_bonus =(empleado["Tipo de contrato"] in ["Termino indefinido", "Termino fijo"] and
                    empleado["Rendimiento"] >= 4.0 and
                    empleado["Permanencia"] >= 12)

print(performance_bonus)

leadership_program =(empleado["Rendimiento"] >= 4.5 and
                     empleado["Puntaje de desempeño"] >= 80) and (
                         empleado["Registro disciplinario"] == "No" or empleado["Nominación manager"] == "Si")

print(leadership_program)

wellness_program =(empleado["Nivel de estres"] > 7 or empleado["Puntaje de desempeño"] < 60) and (
    empleado["Nominación manager"] == "Si"
    )
                
print(wellness_program)

education_benefits = (empleado["Tipo de contrato"] == "Termino indefinido" and
                      empleado["Permanencia"] >= 12 and
                      empleado["Rendimiento"] >= 4.0 and
                      empleado["Programa relacionado con el trabajo"] == "Si")

print(education_benefits)
