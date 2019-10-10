import tkinter

from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame

from database.database import Database
from tables.table import Table
from tables.schema import client_table
from tables.schema import vehicle_table
from tables.schema import repair_table



# def app():
#     conn = Database.connect()
#     if conn:
#         table = Table(conn)
#         table.create(client_table)
#         table.create(vehicle_table)
#         table.create(repair_table)
#         values = {'name':'sofia', 'last_name':"garcia", 'identification_number':"19.257.652", 'email':"ceh@gmail.com", 'phone':"6566", 'address':"Vzla"}
#         table.insert_data("client", values)
#         table.show_all("client")
#     else:
#         print("Error! cannot create the database connection.")

#app()

import tkinter

from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame
from tkinter import Frame


window = tkinter.Tk()
window.geometry('800x500')

#client_frame = LabelFrame(window,text="Detalles del Cliente")
#client_frame.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
client_frame = LabelFrame(window,text="Detalles del Cliente")
client_frame.grid(row=0, columnspan=4)


name_label = Label(client_frame,text = "Nombre").grid(row = 0, column = 0)
# last_name_label = Label(client_frame ,text = "Apellido").grid(row = 1,column = 0)
# id_label = Label(client_frame ,text = "C.I").grid(row = 2,column = 0)
# email_label = Label(client_frame ,text = "Email").grid(row = 3,column = 0)
# phone_label = Label(client_frame ,text = "Teléfono").grid(row = 4,column = 0)
# address_label = Label(client_frame ,text = "Dirección").grid(row = 5,column = 0)
#
name = tkinter.StringVar()
# last_name = tkinter.StringVar()
# id = tkinter.StringVar()
# email = tkinter.StringVar()
# phone = tkinter.StringVar()
# address = tkinter.StringVar()


name_data = Entry(client_frame, textvariable=name).grid(row=0, column=1)
# last_name_data = Entry(client_frame, textvariable=last_name).grid(row = 1,column = 1 )
# id_data = Entry(client_frame, textvariable=id).grid(row = 2,column = 5)
# email_data = Entry(client_frame, textvariable=email).grid(row = 3,column = 1)
# phone_data = Entry(client_frame, textvariable=phone).grid(row = 4,column = 1)
# address_data = Entry(client_frame, textvariable=address).grid(row = 5,column = 1)
#
# # vehicle_frame = LabelFrame(window,text="Detalles del Vehiculo")
# # vehicle_frame.grid(row=8, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
# #
# # model_label = Label(vehicle_frame,text = "Modelo").grid(row = 8,column = 0)
# # mileage_label = Label(vehicle_frame,text = "Kilometraje").grid(row = 9,column = 0)
#
# def test():
#     dict = {"name": name.get(),
#             "last_name": last_name.get(),
#             "id": id.get(),
#             "email": email.get(),
#             "phone": phone.get(),
#             "address": address.get()
#             }
#     print(dict)

# submit = Button(window, text = 'Guardar', command = test).grid(row = 7,column = 0)

client_frame.pack()

window.mainloop()
