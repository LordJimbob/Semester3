import tkinter as tk

def opdater_tal(op):
    global tal
    if op == "stig":
        tal += 1
    elif op == "fald":
        tal -= 1
    label.config(text=f"Tal: {tal}")

tal = 0

root = tk.Tk()
root.title("Talstyring")

label = tk.Label(root, text=f"Tal: {tal}")
label.pack(pady=10)

stig_knap = tk.Button(root, text="Stig", command=lambda: opdater_tal("stig"))
stig_knap.pack()

fald_knap = tk.Button(root, text="Fald", command=lambda: opdater_tal("fald"))
fald_knap.pack()

root.mainloop()
