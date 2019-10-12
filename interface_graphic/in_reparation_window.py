from tkinter import *
import tkinter.ttk as ttk


class InReparationWindow:
    """Class for window to repair"""

    def __init__(self):
        root = Tk()
        root.title('Vehiculos en Reparacion')

        list_headers = ['vehiculo', 'placa', 'cliente']
        list_values = [
        ('Aveo', 'AZ-OIUYG', "Maria Perez") ,
        ('Spark', 'FR-9874', "Jose Perez") ,
        ('Lacetti', 'WA-8764', 'Luis Rodriguez') ,
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Aveo', 'AZ-OIUYG', "Maria Perez"),
        ('Spark', 'FR-9874', "Jose Perez"),
        ('Lacetti', 'WA-8764', 'Luis Rodriguez'),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Aveo', 'AZ-OIUYG', "Maria Perez"),
        ('Spark', 'FR-9874', "Jose Perez"),
        ('Lacetti', 'WA-8764', 'Luis Rodriguez'),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Aveo', 'AZ-OIUYG', "Maria Perez"),
        ('Spark', 'FR-9874', "Jose Perez"),
        ('Lacetti', 'WA-8764', 'Luis Rodriguez'),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza"),
        ('Cruze', 'BO-123D6', "Marcos Mendoza")
        ]

        client_frame = LabelFrame(root, text="Vehiculos en Reparacion")
        client_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        tree = ttk.Treeview(client_frame, columns=list_headers, show="headings")
        tree.grid(row=0, column=0, padx=5, pady=5)
        vsb = ttk.Scrollbar(client_frame, orient="vertical", command=tree.yview)
        vsb.grid(row=0, column=1, sticky='ns')

        tree.configure(yscrollcommand=vsb.set)


        for col in list_headers:
            tree.heading(col, text=col.title())
        for item in list_values:
            tree.insert('', 'end', values=item)

        def selectItem():
            curItem = tree.focus()
            print(tree.item(curItem))
            tree.delete(curItem)


        btn = Button(root, text="Finalizar Reparacion", command=selectItem)
        btn.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        mainloop()