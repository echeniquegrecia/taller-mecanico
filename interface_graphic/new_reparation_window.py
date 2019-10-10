from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class NewReparationWindow:
    """Class for window to repair"""

    def __init__(self):
        root = Tk()
        root.title('Reparación vehículo')


        name = StringVar()
        last_name = StringVar()
        id = StringVar()
        email = StringVar()
        phone = StringVar()
        address = StringVar()
        brand = StringVar()

        model = StringVar()
        mileage = StringVar()
        year = StringVar()
        color = StringVar()
        car_id = StringVar()
        date_arrival = StringVar()

        search_car_frame = LabelFrame(root, text="Busqueda")
        search_car_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W)

        client_frame = LabelFrame(root, text="Detalles del Cliente")
        client_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)
        vehicle_frame = LabelFrame(root, text="Detalles del Vehículo")
        vehicle_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)

        reparacion_frame = LabelFrame(root, text="Reparacion")
        reparacion_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)

        date_frame = Frame(reparacion_frame)
        date_frame.grid(row=3, column=0, columnspan=4, padx=0, pady=0, sticky=W)

        button_frame = Frame(root)
        button_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky=E+N)



        search_car_label = Label(search_car_frame, text="Placa")
        search_car_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        name_label = Label(client_frame, text="Nombre", width=20)
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        last_name_label = Label(client_frame, text="Apellido", width=20)
        last_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        id_label = Label(client_frame, text="C.I", width=20)
        id_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        email_label = Label(client_frame, text="Email", width=20)
        email_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        phone_label = Label(client_frame, text="Teléfono", width=20)
        phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        address_label = Label(client_frame, text="Dirección", width=20)
        address_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        brand_label = Label(vehicle_frame, text="Marca", width=20)
        brand_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        model_label = Label(vehicle_frame, text="Modelo", width=20)
        model_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        mileage_label = Label(vehicle_frame, text="Kilometraje", width=20)
        mileage_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        year_label = Label(vehicle_frame, text="Año", width=20)
        year_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        color_label = Label(vehicle_frame, text="Color", width=20)
        color_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        car_id_label = Label(vehicle_frame, text="Placa", width=20)
        car_id_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        observations_client_label = Label(reparacion_frame, text="Observaciones previas del cliente:")
        observations_client_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        observations_mechanic_label = Label(reparacion_frame, text="Observaciones previas del mecanico:")
        observations_mechanic_label.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        date_arrival_label = Label(date_frame, text="Fecha de entrada (M-D-Y)")
        date_arrival_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)


        search_car_entry = Combobox(search_car_frame, width=20, textvariable=car_id)
        search_car_entry["values"] = ("AW125-G", "OY678-2", "UYHF-25")
        search_car_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        name_entry = Entry(client_frame, width=30, textvariable=name)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        last_name_entry = Entry(client_frame, width=30, textvariable=last_name)
        last_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        id_entry = Entry(client_frame, width=30, textvariable=id)
        id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        email_entry = Entry(client_frame, width=30, textvariable=email)
        email_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        phone_entry = Entry(client_frame, width=30, textvariable=phone)
        phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        address_entry = Entry(client_frame, width=30, textvariable=address)
        address_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        brand_entry = Entry(vehicle_frame, width=30, textvariable=brand)
        brand_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        model_entry = Entry(vehicle_frame, width=30, textvariable=model)
        model_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        mileage_entry = Entry(vehicle_frame, width=30, textvariable=mileage)
        mileage_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        year_entry = Entry(vehicle_frame, width=30, textvariable=year)
        year_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        color_entry = Entry(vehicle_frame, width=30, textvariable=color)
        color_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        car_id_entry = Entry(vehicle_frame, width=30, textvariable=car_id)
        car_id_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        observations_client = Text(reparacion_frame, width=42, height = 5)
        observations_client.grid(row=1, column=0,padx=5, pady=5, sticky=W)

        observations_mecanico = Text(reparacion_frame, width=42, height = 5)
        observations_mecanico.grid(row=1, column=1, columnspan=2,padx=5, pady=5, sticky=W)

        date_arrival_entry = DateEntry(date_frame, width=12, background='darkblue',foreground='white', borderwidth=2, year=2019, textvariable=date_arrival)
        date_arrival_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        def edit_vehicle():
            dict = {"name": name.get(),
                    "last_name": last_name.get(),
                    "id": id.get(),
                    "email": email.get(),
                    "phone": phone.get(),
                    "address": address.get(),
                    "brand": brand.get(),
                    "model": model.get(),
                    "mileage": mileage.get(),
                    "year": year.get(),
                    "color": color.get(),
                    "car_id": car_id.get(),
                    "date_arrival": date_arrival.get()
                    }
            print(dict)

        button = Button(button_frame, text="Crear Reparacion", command=edit_vehicle)
        button.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        search_car_frame.grid_columnconfigure(1, weight=1)
        search_car_frame.grid_rowconfigure(1, weight=1)

        client_frame.grid_columnconfigure(1, weight=1)
        client_frame.grid_rowconfigure(1, weight=1)
        vehicle_frame.grid_columnconfigure(1, weight=1)
        vehicle_frame.grid_rowconfigure(1, weight=1)

        reparacion_frame.grid_columnconfigure(1, weight=1)

        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)

        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.mainloop()
