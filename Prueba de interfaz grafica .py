import easygui

# Mensaje de bienvenida
easygui.msgbox("¡Bienvenido a mi programa con EasyGui!", "Mi Programa")

# Pregunta al usuario su nombre
user_name = easygui.enterbox("¿Cuál es tu nombre?", "Introduce tu nombre")

# Muestra un saludo personalizado
easygui.msgbox(f"¡Hola, {user_name}!", "Saludo Personalizado")

# Pregunta al usuario su edad
user_age = easygui.integerbox("¿Cuántos años tienes?", "Introduce tu edad", lowerbound=0)

# Muestra un mensaje basado en la edad
if user_age is not None:
    if user_age < 18:
        easygui.msgbox("Eres menor de edad.", "Información")
    else:
        easygui.msgbox("Eres mayor de edad.", "Información")
else:
    easygui.msgbox("No ingresaste una edad válida.", "Error")
