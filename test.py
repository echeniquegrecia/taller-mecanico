# import tkinter as tk
# from tkinter import ttk
# from tkcalendar import DateEntry
# from datetime import date
#
# root = tk.Tk()
# # change ttk theme to 'clam' to fix issue with downarrow button
# style = ttk.Style(root)
# style.theme_use('clam')
#
# class MyDateEntry(DateEntry):
#     def __init__(self, master=None, **kw):
#         DateEntry.__init__(self, master=None, **kw)
#         # add black border around drop-down calendar
#         self._top_cal.configure(bg='black', bd=1)
#         # add label displaying today's date below
#         tk.Label(self._top_cal, bg='gray90', anchor='w',
#                  text='Today: %s' % date.today().strftime('%x')).pack(fill='x')
#
# # create the entry and configure the calendar colors
# de = MyDateEntry(root, year=2018, month=8, day=11,
#                  selectbackground='gray80',
#                  selectforeground='black',
#                  normalbackground='white',
#                  normalforeground='black',
#                  background='gray90',
#                  foreground='black',
#                  bordercolor='gray90',
#                  othermonthforeground='gray50',
#                  othermonthbackground='white',
#                  othermonthweforeground='gray50',
#                  othermonthwebackground='white',
#                  weekendbackground='white',
#                  weekendforeground='black',
#                  headersbackground='white',
#                  headersforeground='gray70')
#
#
# if __name__ == '__main__':
#     de.pack()
#     root.mainloop()


try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry


def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)

    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def example2():

    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()


def example3():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2010)
    cal.pack(padx=10, pady=10)


root = tk.Tk()
ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

root.mainloop()