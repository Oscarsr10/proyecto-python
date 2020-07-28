"""
Proyecto Python y MySQL:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "Registro":
    hazEl.registro()
    

elif accion == "Login":
    hazEl.login()