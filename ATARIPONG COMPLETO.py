import tkinter as tk

# -------------------------
# CONFIGURACIÓN
# -------------------------

ANCHO = 800
ALTO = 500

VENTANA = tk.Tk()
VENTANA.title("Atari Pong - Tkinter")

canvas = tk.Canvas(VENTANA, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

# -------------------------
# OBJETOS
# -------------------------

pala_izq = canvas.create_rectangle(20, 200, 30, 300, fill="white")
pala_der = canvas.create_rectangle(770, 200, 780, 300, fill="white")

pelota = canvas.create_oval(390, 240, 410, 260, fill="white")

# Línea central
canvas.create_line(400, 0, 400, 500, fill="white", dash=(10, 10))

# -------------------------
# VARIABLES
# -------------------------

vel_x = 4
vel_y = 4
vel_pala = 20

puntos_izq = 0
puntos_der = 0

texto_puntos = canvas.create_text(
    400,
    30,
    text="0     0",
    fill="white",
    font=("Arial", 24)
)

# -------------------------
# FUNCIONES
# -------------------------

def actualizar_marcador():
    canvas.itemconfig(
        texto_puntos,
        text=f"{puntos_izq}     {puntos_der}"
    )


def reiniciar_pelota():
    global vel_x, vel_y

    canvas.coords(pelota, 390, 240, 410, 260)

    if vel_x > 0:
        vel_x = -4
    else:
        vel_x = 4

    vel_y = 4


def choque(pala, pelota_pos):

    pos_pala = canvas.coords(pala)

    return not(
        pelota_pos[2] < pos_pala[0]
        or pelota_pos[0] > pos_pala[2]
        or pelota_pos[3] < pos_pala[1]
        or pelota_pos[1] > pos_pala[3]
    )


def mover_pala(event):

    tecla = event.keysym

    if tecla == "w":

        pos = canvas.coords(pala_izq)

        if pos[1] > 0:
            canvas.move(pala_izq, 0, -vel_pala)

    elif tecla == "s":

        pos = canvas.coords(pala_izq)

        if pos[3] < ALTO:
            canvas.move(pala_izq, 0, vel_pala)

    elif tecla == "Up":

        pos = canvas.coords(pala_der)

        if pos[1] > 0:
            canvas.move(pala_der, 0, -vel_pala)

    elif tecla == "Down":

        pos = canvas.coords(pala_der)

        if pos[3] < ALTO:
            canvas.move(pala_der, 0, vel_pala)


VENTANA.bind("<Key>", mover_pala)


def mover_pelota():

    global vel_x
    global vel_y
    global puntos_izq
    global puntos_der

    canvas.move(pelota, vel_x, vel_y)

    pos = canvas.coords(pelota)

    # Rebote arriba
    if pos[1] <= 0:
        vel_y = -vel_y

    # Rebote abajo
    if pos[3] >= ALTO:
        vel_y = -vel_y

    # Rebote con las palas
    if choque(pala_izq, pos):
        vel_x = abs(vel_x)

    if choque(pala_der, pos):
        vel_x = -abs(vel_x)

    # Punto jugador derecho
    if pos[0] <= 0:

        puntos_der += 1

        actualizar_marcador()

        reiniciar_pelota()

    # Punto jugador izquierdo
    if pos[2] >= ANCHO:

        puntos_izq += 1

        actualizar_marcador()

        reiniciar_pelota()

    # Ganador
    if puntos_izq == 5:

        canvas.create_text(
            400,
            250,
            text="¡Jugador Izquierdo Gana!",
            fill="yellow",
            font=("Arial", 24)
        )

        return

    if puntos_der == 5:

        canvas.create_text(
            400,
            250,
            text="¡Jugador Derecho Gana!",
            fill="yellow",
            font=("Arial", 24)
        )

        return

    VENTANA.after(20, mover_pelota)


mover_pelota()

VENTANA.mainloop()
