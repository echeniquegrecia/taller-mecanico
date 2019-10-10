from tkinter import *

from interface_graphic.new_vehicle_window import NewVehicleWindow
from interface_graphic.new_reparation_window import NewReparationWindow
from settings import IMAGE_MENU
from PIL import Image, ImageTk

class MenuWindow:
    """Class for new window to create a new vehicle"""

    def __init__(self):
        root = Tk()
        root.title('Taller Mecanico Echenique - Programa de gestion')
        root.state('zoomed')


        image = Image.open(IMAGE_MENU)
        image = ImageTk.PhotoImage(image)
        label = Label(image=image)
        label.grid(row=0, column=0, columnspan=5, padx=120, pady=10, sticky=W+E)

        button_frame = Label(root)
        button_frame.grid(row=2, column=0, padx=5, pady=5, sticky=S)

        button = Button(button_frame, text="Nuevo vehiculo", height=15, width=40, command=NewVehicleWindow)
        button.grid(row=0, column=0, padx=8, pady=10, sticky=W+E)

        button = Button(button_frame, text="Nueva Reparacion", height=15, width=40, command=NewReparationWindow)
        button.grid(row=0, column=1, padx=8, pady=10, sticky=W+E)

        button = Button(button_frame, text="Vehiculos en Reparacion", height=15, width=40)
        button.grid(row=0, column=2, padx=8, pady=10, sticky=W+E)

        button = Button(button_frame, text="Historial de Vehiculos", height=15, width=40)
        button.grid(row=0, column=3, padx=8, pady=10, sticky=W+E)

        button = Button(button_frame, text="Historial de Reparaciones", height=15, width=40)
        button.grid(row=0, column=4, padx=5, pady=5, sticky=W+E)

        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)

        root.mainloop()

MenuWindow()