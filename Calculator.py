from tkinter import *


def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    title_bar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + title_bar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def click(event):
    string = sc_value.get()
    if string == "Error":
        sc_value.set("")
        screen.update()
    text = event.widget.cget("text")
    if text == "=":
        try:
            if sc_value.get().isdigit():
                value = float(sc_value.get())
            else:
                value = eval(screen.get())
            sc_value.set(value)
            screen.update()
        except Exception as e:
            print(e)
            sc_value.set("Error")
            screen.update()
    elif text == "C":
        if string == "Error":
            sc_value.set("")
            screen.update()
        else:
            s = string[0: len(string) - 1]
            sc_value.set(s)
            screen.update()
    elif text == "AC":
        sc_value.set("")
        screen.update()
    elif text == "×":
        sc_value.set(sc_value.get() + "*")
    elif text == "÷":
        sc_value.set(sc_value.get() + "/")
    elif text == "+/-":
        value = sc_value.get()
        if value.isdigit() or value.isdecimal():
            value = int(value)
            value *= -1
            sc_value.set(value)
            screen.update()
        else:
            try:
                value = float(value)
                value *= -1
                sc_value.set(value)
                screen.update()
            except Exception as e:
                print(e)
                try:
                    idx = 0
                    ans: str = ""
                    for i in range(len(string)-1, 0-1, -1):
                        if value[i] != '/' and value[i] != '*' and value[i] != '+' and value[i] != '-':
                            ans = value[i] + ans
                        else:
                            idx = i
                            break

                    a = float(ans)
                    a *= -1
                    if idx != 0:
                        sc_value.set(value[0:idx + 1] + "(" + str(a) + ")")
                    else:
                        sc_value.set(value[0:idx] + "(" + str(a) + ")")
                except Exception as e:
                    print(e)
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()






if __name__ == '__main__':
    root = Tk()
    root.geometry("450x550")
    root.title("Calculator")
    root.resizable(False, False)
    root.wm_iconbitmap("Calculator_Icon.ico")
    center(root)

    sc_value = StringVar()
    sc_value.set("")
    screen = Entry(root, textvar=sc_value, font="Arial 25 normal", fg="Red", state=DISABLED)
    screen.pack(fill=X, ipadx=8, pady=25, padx=25)

    Button_1 = Button(text="C", font="Arial 25 normal", height=1, width=3, bg="Orange")
    Button_1.pack(padx=7, pady=5)
    Button_1.bind("<Button-1>", click)
    Button_1.place(x=30, y=100)

    Button_2 = Button(text="AC", font="Arial 25 normal", height=1, width=3, bg="Orange")
    Button_2.pack(padx=7, pady=5)
    Button_2.bind("<Button-1>", click)
    Button_2.place(x=115, y=100)

    Button_3 = Button(text="+/-", font="Arial 25 normal", height=1, width=3, bg="Orange")
    Button_3.pack(padx=7, pady=5)
    Button_3.bind("<Button-1>", click)
    Button_3.place(x=195, y=100)

    Button_4 = Button(text="(", font="Arial 25 normal", height=1, width=3, bg="Orange")
    Button_4.pack(padx=7, pady=5)
    Button_4.bind("<Button-1>", click)
    Button_4.place(x=275, y=100)

    Button_5 = Button(text=")", font="Arial 25 normal", height=1, width=3, bg="Orange")
    Button_5.pack(padx=7, pady=5)
    Button_5.bind("<Button-1>", click)
    Button_5.place(x=355, y=100)

    Button_6 = Button(text="1", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_6.pack(padx=7, pady=5)
    Button_6.bind("<Button-1>", click)
    Button_6.place(x=30, y=180)

    Button_7 = Button(text="2", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_7.pack(padx=7, pady=5)
    Button_7.bind("<Button-1>", click)
    Button_7.place(x=130, y=180)

    Button_8 = Button(text="3", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_8.pack(padx=7, pady=5)
    Button_8.bind("<Button-1>", click)
    Button_8.place(x=230, y=180)

    Button_9 = Button(text="+", font="Arial 25 normal", height=1, width=4, bg="Orange")
    Button_9.pack(padx=7, pady=5)
    Button_9.bind("<Button-1>", click)
    Button_9.place(x=330, y=180)

    Button_10 = Button(text="4", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_10.pack(padx=7, pady=5)
    Button_10.bind("<Button-1>", click)
    Button_10.place(x=30, y=260)

    Button_11 = Button(text="5", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_11.pack(padx=7, pady=5)
    Button_11.bind("<Button-1>", click)
    Button_11.place(x=130, y=260)

    Button_12 = Button(text="6", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_12.pack(padx=7, pady=5)
    Button_12.bind("<Button-1>", click)
    Button_12.place(x=230, y=260)

    Button_13 = Button(text="-", font="Arial 25 normal", height=1, width=4, bg="Orange")
    Button_13.pack(padx=7, pady=5)
    Button_13.bind("<Button-1>", click)
    Button_13.place(x=330, y=260)

    Button_14 = Button(text="7", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_14.pack(padx=7, pady=5)
    Button_14.bind("<Button-1>", click)
    Button_14.place(x=30, y=340)

    Button_15 = Button(text="8", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_15.pack(padx=7, pady=5)
    Button_15.bind("<Button-1>", click)
    Button_15.place(x=130, y=340)

    Button_16 = Button(text="9", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_16.pack(padx=7, pady=5)
    Button_16.bind("<Button-1>", click)
    Button_16.place(x=230, y=340)

    Button_17 = Button(text="×", font="Arial 25 normal", height=1, width=4, bg="Orange")
    Button_17.pack(padx=7, pady=5)
    Button_17.bind("<Button-1>", click)
    Button_17.place(x=330, y=340)

    Button_18 = Button(text=".", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_18.pack(padx=7, pady=5)
    Button_18.bind("<Button-1>", click)
    Button_18.place(x=30, y=420)

    Button_19 = Button(text="0", font="Arial 25 normal", height=1, width=4, bg="Light Gray")
    Button_19.pack(padx=7, pady=5)
    Button_19.bind("<Button-1>", click)
    Button_19.place(x=130, y=420)

    Button_20 = Button(text="=", font="Arial 25 normal", height=1, width=4, bg="Orange")
    Button_20.pack(padx=7, pady=5)
    Button_20.bind("<Button-1>", click)
    Button_20.place(x=230, y=420)

    Button_21 = Button(text="÷", font="Arial 25 normal", height=1, width=4, bg="Orange")
    Button_21.pack(padx=7, pady=5)
    Button_21.bind("<Button-1>", click)
    Button_21.place(x=330, y=420)

    root.mainloop()
