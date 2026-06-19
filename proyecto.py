import random

# --- Capa de Negocio ---
# Esta función decide qué juega la máquina al azar
def generar_jugada_maquina():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# --- Capa de Control ---
# Esta es la función principal que maneja el juego
def iniciar_juego():
    # Inicializamos puntos
    puntos_usuario = 0
    puntos_maquina = 0
    
    # Bucle simple: el juego corre por 3 rondas (puedes cambiar este número)
    ronda_actual = 1
    while ronda_actual <= 3:
        print(f"\n--- Ronda {ronda_actual} ---")
        
        # Entrada del usuario
        jugada = input("Elige piedra, papel o tijera: ").lower()
        maquina = generar_jugada_maquina()
        print(f"La máquina eligió: {maquina}")
        
        # Lógica: Comparamos para ver quién gana
        # Estructura condicional (if/elif/else)
        if jugada == maquina:
            print("Resultado: Empate")
        elif (jugada == "piedra" and maquina == "tijera") or \
             (jugada == "papel" and maquina == "piedra") or \
             (jugada == "tijera" and maquina == "papel"):
            print("Resultado: ¡Ganaste esta ronda!")
            puntos_usuario = puntos_usuario + 1
        else:
            print("Resultado: Perdiste esta ronda")
            puntos_maquina = puntos_maquina + 1
            
        ronda_actual = ronda_actual + 1

    # Mostramos el resultado final después del bucle
    print("\n--- Juego terminado ---")
    print(f"Puntaje Final -> Usuario: {puntos_usuario} | Máquina: {puntos_maquina}")

# Ejecutamos la función
iniciar_juego()