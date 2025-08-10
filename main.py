import tkinter as tk


def tus_tikla(tus):
    if tus == "=":
        try:
            sonuc = str(eval(ekran.get()))
            ekran.delete(0, tk.END)
            ekran.insert(tk.END, sonuc)
        except:
            ekran.delete(0, tk.END)
            ekran.insert(tk.END, "Hata")
    elif tus == "C":
        ekran.delete(0, tk.END)
    else:
        ekran.insert(tk.END, tus)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

ekran = tk.Entry(pencere, width=20, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
ekran.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


butonlar = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

satir = 1
sutun = 0
for tus in butonlar:
    tk.Button(pencere, text=tus, width=5, height=2, font=("Arial", 14),
              command=lambda t=tus: tus_tikla(t)).grid(row=satir, column=sutun, padx=2, pady=2)
    sutun += 1
    if sutun > 3:
        sutun = 0
        satir += 1

tk.Button(pencere, text="C", width=5, height=2, font=("Arial", 14),
          command=lambda: tus_tikla("C")).grid(row=satir, column=0, padx=2, pady=2)


pencere.mainloop()