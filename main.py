from tkinter import *

num_sub = 0
all_sval = []
all_values = []
data = {}


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


def sgpa_calc(data):
    eci = 0
    ecigi = 0
    for key, value in data.items():
        eci += value[0]
        ecigi += value[0] * value[3]
    sgpa = round(ecigi / eci, 2)
    return sgpa


def clear1():
    global num_sub
    num_sub = int(entry1.get())
    for wid in frame.winfo_children():
        wid.destroy()
    for n in range(num_sub):
        Label(frame, text=f"Enter subject {n + 1}: ").grid(row=n, column=0)
        sentry = Entry(frame, width=15)
        sentry.grid(row=n, column=1)
        all_sval.append(sentry)
    Button(frame, text="Enter", command=clear2, width=12).grid(row=num_sub, column=0, columnspan=2)


def clear2():
    global all_values
    global data
    all_values = []
    data = {}
    try:
        for n in range(num_sub):
            all_sval[n] = all_sval[n].get()
    except AttributeError:
        pass
    for wid in frame.winfo_children():
        wid.destroy()
    Label(frame, text="Subjects").grid(row=0, column=0)
    Label(frame, text="Credits").grid(row=0, column=1)
    Label(frame, text="Marks").grid(row=0, column=2)
    Label(frame, text="Grade").grid(row=0, column=3)
    for n in range(num_sub):
        lst = []
        Label(frame, text=f"{all_sval[n]}: ").grid(row=n + 1, column=0)
        centry = Entry(frame, width=15)
        centry.grid(row=n + 1, column=1)
        lst.append(centry)
        mentry = Entry(frame, width=15)
        mentry.grid(row=n + 1, column=2)
        lst.append(mentry)
        all_values.append(lst)
    Button(frame, text="Calculate", command=clear3, width=12).grid(row=num_sub+2, column=0, columnspan=2)


def clear3():
    for lst in all_values:
        for n in range(len(lst)):
            lst[n] = int(lst[n].get())
    for n in range(len(all_sval)):
        grade, gp = grade_calc(all_values[n][1])
        all_values[n].append(grade)
        all_values[n].append(gp)
        data[all_sval[n]] = all_values[n]
    for n in range(num_sub):
        Label(frame, text=all_values[n][2]).grid(row=n+1, column=3)
    Label(frame, text=f"Your SGPA is {sgpa_calc(data)}").grid(row=num_sub+1, column=0, columnspan=3)
    Button(frame, text="Calculate again", command=clear2, width=12).grid(row=num_sub+2, column=2, columnspan=2)


window = Tk()
window.config(padx=20, pady=20)
window.title("SGPA Calculator")

# Frame
frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")

# Labels
Label(frame, text="SGPA Calculator").grid(row=0, column=0)
Label(frame, text="Enter the number of subjects below:").grid(row=1, column=0)

# Entries
entry1 = Entry(frame, width=14)
entry1.focus()
entry1.grid(row=2, column=0)

# Buttons
button1 = Button(frame, text="Enter", command=clear1, width=12)
button1.grid(row=3, column=0)

window.mainloop()
