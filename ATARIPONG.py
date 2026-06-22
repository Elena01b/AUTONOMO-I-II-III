import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Atari Pong - Sin Pygame")

ANCHO = 800
ALTO = 500

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

# Paletas
pala_izq = canvas.create_rectangle(20, 200, 30, 300, fill="white")
pala_der = canvas.create_rectangle(770, 200, 780, 300, fill="white")

# Pelota
pelota = canvas.create_oval(390, 240, 410, 260, fill="white")

# Movimiento pelota
vel_x = 4
vel_y = 4

# Movimiento palas
vel_pala = 20

# Funciones de movimiento
def mover_pala(event):
    tecla = event.keysym

    if tecla == "w":
        canvas.move(pala_izq, 0, -vel_pala)
    elif tecla == "s":
        canvas.move(pala_izq, 0, vel_pala)
    elif tecla == "Up":
        canvas.move(pala_der, 0, -vel_pala)
    elif tecla == "Down":
        canvas.move(pala_der, 0, vel_pala)

# Detectar teclas
ventana.bind("<Key>", mover_pala)

# Animación del juego
def mover_pelota():
    global vel_x, vel_y

    canvas.move(pelota, vel_x, vel_y)
    pos = canvas.coords(pelota)

    # Rebote arriba y abajo
    if pos[1] <= 0 or pos[3] >= ALTO:
        vel_y = -vel_y

    # Rebote con palas
    if choque(pala_izq, pos) or choque(pala_der, pos):
        vel_x = -vel_x

    # Reinicio si sale
    if pos[0] <= 0 or pos[2] >= ANCHO:
        canvas.coords(pelota, 390, 240, 410, 260)

    ventana.after(20, mover_pelota)

def choque(pala, pelota_pos):
    pos_pala = canvas.coords(pala)

    return not (
        pelota_pos[2] < pos_pala[0] or
        pelota_pos[0] > pos_pala[2] or
        pelota_pos[3] < pos_pala[1] or
        pelota_pos[1] > pos_pala[3]
    )

mover_pelota()

ventana.mainloop()