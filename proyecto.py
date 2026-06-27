import random

# --- Capa de Negocio ---
def generar_jugada_maquina():
    opciones = ["piedra", "papel", "tijera"] # Lista para cumplir con lo solicitado
    return random.choice(opciones)

# --- Capa de Control ---
def iniciar_juego():
    print("=== BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA ===")
    puntos_usuario = 0
    puntos_maquina = 0
    
    rondas = 3
    for ronda_actual in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda_actual} de {rondas} ---")
        
        # Validamos la entrada para que sea segura
        while True:
            jugada = input("Elige piedra, papel o tijera: ").lower().strip()
            if jugada in ["piedra", "papel", "tijera"]:
                break
            print(">> Error: Entrada no válida, intenta otra vez.")
        
        maquina = generar_jugada_maquina()
        print(f"La máquina eligió: {maquina}")
        
        # Lógica de juego
        if jugada == maquina:
            print("Resultado: Empate")
        elif (jugada == "piedra" and maquina == "tijera") or \
             (jugada == "papel" and maquina == "piedra") or \
             (jugada == "tijera" and maquina == "papel"):
            print("Resultado: ¡Ganaste esta ronda!")
            puntos_usuario += 1
        else:
            print("Resultado: Perdiste esta ronda")
            puntos_maquina += 1

    # Resultado final
    print("\n" + "="*30)
    print("JUEGO TERMINADO")
    print(f"Marcador Final -> Tú: {puntos_usuario} | Máquina: {puntos_maquina}")
    print("="*30)

# Ejecución
iniciar_juego()