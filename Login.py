import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Main window")
window.geometry("600x600")
canvas = tkinter.Canvas(width=600, height=600, bg='#83c0ec')

#login
login_l = tkinter.Label(text="логин")
login_l.place(x=220, y=20)

login = tkinter.StringVar()
login_e = tkinter.Entry(textvariable=login)
login_e.place(x=220, y=50)

#password
pas_l = tkinter.Label(text="пароль")
pas_l.place(x=220, y=80)

pas = tkinter.StringVar()
pas_e = tkinter.Entry(textvariable=pas)
pas_e.place(x=220, y=110)

#button
def success_func():
    l = login.get()
    p = pas.get()
    if len(l) > 0 and l.replace(" ", ""):
        messagebox.showinfo(title="Успешный Вход!", message="Ваши данные были украдены и проданы!")
    else:
        messagebox.showinfo(title="Отказано", message="неправильный логин или пароль")
def er_fuc():
    window.destroy()
    messagebox.showinfo(title="Успешный Выход!", message="Неприятность")

b_s = tkinter.Button(text="Вход", command=success_func)
b_s.place(x=200, y=140)

nazad = tkinter.Button(text="Отмена", command=er_fuc)
nazad.place(x=320, y=140)

canvas.pack()
window.mainloop()