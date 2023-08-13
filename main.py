from tkinter import *

num_sub = 0
all_sval = []
credit_entries = []
marks_entries = []
data = {}
calc = None
entry1 = None


def grade_calc(m):
    if 90 <= m <= 100:
        return "S", 10
    elif 80 <= m < 90:
        return "A", 9
    elif 70 <= m < 80:
        return "B", 8
    elif 60 <= m < 70:
        return "C", 7
    elif 45 <= m < 60:
        return "D", 6
    elif 40 <= m < 45:
        return "E", 4
    elif m < 40:
        return "F", 0


def sgpa_calc(d):
    eci = 0
    ecigi = 0
    for key, value in d.items():
        eci += value[0]
        ecigi += value[0] * value[3]
    sgpa = round(ecigi / eci, 2)
    return sgpa


def create_win(w_width, w_height):
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()
    x = s_width//2 - w_width//2
    y = s_height//2 - w_height//2 - 100
    window.geometry(f"{w_width}x{w_height}+{x}+{y}")


def phase1():
    global entry1
    Label(window, text="SGPA Calculator").place(relx=0.5, rely=0.3, anchor=CENTER)
    Label(window, text="Enter the number of subjects below:").place(relx=0.5, rely=0.4, anchor=CENTER)
    entry1 = Entry(window, width=14)
    entry1.focus()
    entry1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button1 = Button(window, text="Enter", command=phase2, width=12)
    button1.place(relx=0.5, rely=0.6, anchor=CENTER)


def phase2():
    global num_sub
    num_sub = int(entry1.get())
    for wid in window.winfo_children():
        wid.destroy()
    width = 300
    height = 50*(num_sub+1)
    create_win(width, height)
    div = 1.0/(num_sub+2)
    y = div
    for n in range(num_sub):
        Label(window, text=f"Enter subject {n + 1}: ").place(relx=0.25, rely=y, anchor=CENTER)
        sentry = Entry(window, width=15)
        sentry.place(relx=0.75, rely=y, anchor=CENTER)
        all_sval.append(sentry)
        y += div
    Button(window, text="Enter", command=phase3, width=12).place(relx=0.5, rely=y, anchor=CENTER)


def phase3():
    global data
    global calc
    data = {}
    for n in range(num_sub):
        all_sval[n] = all_sval[n].get()
    for wid in window.winfo_children():
        wid.destroy()
    width = 400
    height = 50*(num_sub+2)
    create_win(width, height)
    div = 1.0 / (num_sub + 4)
    y = div
    Label(window, text="Subjects").place(relx=0.125, rely=y, anchor=CENTER)
    Label(window, text="Credits").place(relx=0.375, rely=y, anchor=CENTER)
    Label(window, text="Marks").place(relx=0.625, rely=y, anchor=CENTER)
    Label(window, text="Grade").place(relx=0.875, rely=y, anchor=CENTER)
    y += div
    for n in range(num_sub):
        Label(window, text=f"{all_sval[n]}: ").place(relx=0.125, rely=y, anchor=CENTER)
        centry = Entry(window, width=15)
        centry.place(relx=0.375, rely=y, anchor=CENTER)
        credit_entries.append(centry)
        mentry = Entry(window, width=15)
        mentry.place(relx=0.625, rely=y, anchor=CENTER)
        marks_entries.append(mentry)
        y += div
    calc = Button(window, text="Calculate", command=phase4, width=12)
    calc.place(relx=0.5, rely=y, anchor=CENTER)


def phase4():
    global calc
    credit = []
    mark = []
    for ent in credit_entries:
        credit.append(int(ent.get()))
    for ent in marks_entries:
        mark.append(int(ent.get()))
    for n in range(len(all_sval)):
        grade, gp = grade_calc(mark[n])
        all_values = [credit[n], mark[n], grade, gp]
        data[all_sval[n]] = all_values
    div = 1.0 / (num_sub + 4)
    y = div*2
    for key, value in data.items():
        Label(window, text=value[2]).place(relx=0.875, rely=y, anchor=CENTER)
        y += div
    Label(window, text=f"Your SGPA is {sgpa_calc(data)}").place(relx=0.5, rely=y+div, anchor=CENTER)
    calc.destroy()
    calc = Button(window, text="Calculate", command=phase4, width=12)
    calc.place(relx=0.5, rely=y, anchor=CENTER)


window = Tk()
window.title("SGPA Calculator")
create_win(300, 270)


phase1()
window.mainloop()
