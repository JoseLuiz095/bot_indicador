from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"x={x}, y={y}")

# Cria um ouvinte para eventos do mouse
listener = mouse.Listener(on_click=on_click)

# Inicia o ouvinte
listener.start()

try:
    # Mantém o programa em execução
    listener.join()

except KeyboardInterrupt:
    # Interrompe o ouvinte quando o usuário pressiona Ctrl+C
    listener.stop()
    listener.join()
    print("Programa interrompido pelo usuário.")
