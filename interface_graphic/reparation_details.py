from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class ReparationDetailsWindow:
    """Class for window to repair"""

    def __init__(self):
        root = Tk()
        root.title('Reparación vehículo')
        root.state('zoomed')


        name = StringVar()
        last_name = StringVar()
        id = StringVar()
        email = StringVar()
        phone = StringVar()
        address = StringVar()
        brand = StringVar()
        #
        model = StringVar()
        mileage = StringVar()
        year = StringVar()
        color = StringVar()
        car_id = StringVar()
        date_arrival = StringVar()

        frame = Frame(root, width=1000, height=300)
        frame.grid(row=0, column=0, sticky=N+W)

        frame1 = LabelFrame(frame, width=500, background="bisque")
        frame1.grid(row=0, column=0, padx=5, pady=5, sticky=N+W)

        frame2 = LabelFrame(frame, width=500, background="blue")
        frame2.grid(row=0, column=1, padx=5, pady=5, sticky=N+W)



        client_frame = LabelFrame(frame1, text="Detalles del Cliente")
        client_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)
        vehicle_frame = LabelFrame(frame1, text="Detalles del Vehículo")
        vehicle_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)
        observation_final_frame = LabelFrame(frame1, text="Observacion final")
        observation_final_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=W)


        #
        reparacion_frame = LabelFrame(frame2)
        reparacion_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W+N)
        #
        # date_frame = Frame(reparacion_frame)
        # date_frame.grid(row=3, column=0, columnspan=4, padx=0, pady=0, sticky=W)
        #
        # button_frame = Frame(root)
        # button_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky=E+N)
        #
        #
        name_label = Label(client_frame, text="Nombre")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        last_name_label = Label(client_frame, text="Apellido")
        last_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        id_label = Label(client_frame, text="C.I")
        id_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        email_label = Label(client_frame, text="Email")
        email_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        phone_label = Label(client_frame, text="Teléfono")
        phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        address_label = Label(client_frame, text="Dirección")
        address_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        brand_label = Label(vehicle_frame, text="Marca")
        brand_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        model_label = Label(vehicle_frame, text="Modelo")
        model_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        mileage_label = Label(vehicle_frame, text="Kilometraje")
        mileage_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        year_label = Label(vehicle_frame, text="Año")
        year_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        color_label = Label(vehicle_frame, text="Color")
        color_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        car_id_label = Label(vehicle_frame, text="Placa")
        car_id_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        #

        date_arrival_label = Label(frame2, text="Fecha de entrada:")
        date_arrival_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        observations_client_label = Label(frame2, text="Observaciones previas del cliente:")
        observations_client_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        observations_mechanic_label = Label(frame2, text="Observaciones previas del mecanico:")
        observations_mechanic_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        observations_final_label = Label(observation_final_frame, text="Mecanico:")
        observations_final_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        #
        # date_arrival_label = Label(date_frame, text="Fecha de entrada (M-D-Y)")
        # date_arrival_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        #
        #
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
        #
        observations_client = Text(frame2, width=42, height=8)
        observations_client.grid(row=2, column=0,padx=5, pady=5, sticky=S)

        observations_mecanico = Text(frame2, width=42, height=8)
        observations_mecanico.grid(row=4, column=0, columnspan=2,padx=5, pady=5, sticky=S)

        observations_final = Text(observation_final_frame, height=4, width=63)
        observations_final.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        # def edit_vehicle():
        #     dict = {"name": name.get(),
        #             "last_name": last_name.get(),
        #             "id": id.get(),
        #             "email": email.get(),
        #             "phone": phone.get(),
        #             "address": address.get(),
        #             "brand": brand.get(),
        #             "model": model.get(),
        #             "mileage": mileage.get(),
        #             "year": year.get(),
        #             "color": color.get(),
        #             "car_id": car_id.get(),
        #             "date_arrival": date_arrival.get()
        #             }
        #     print(dict)
        #
        # button = Button(button_frame, text="Crear Reparacion", command=edit_vehicle)
        # button.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        #
        #
        # client_frame.grid_columnconfigure(1, weight=1)
        # client_frame.grid_rowconfigure(1, weight=1)
        # vehicle_frame.grid_columnconfigure(1, weight=1)
        # vehicle_frame.grid_rowconfigure(1, weight=1)
        #
        # reparacion_frame.grid_columnconfigure(1, weight=1)
        #
        # button_frame.grid_columnconfigure(1, weight=1)
        # button_frame.grid_rowconfigure(1, weight=1)
        #
        # root.grid_columnconfigure(1, weight=1)
        # root.grid_rowconfigure(1, weight=1)
        root.mainloop()

ReparationDetailsWindow()