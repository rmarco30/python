import tkinter as tk
from subnet import *
import math


def calculate():

	try:
		network = Network(entry_ip.get(), entry_host.get())
		
		text.delete(1.0, tk.END)
		text.insert(tk.END, f"{network.bits()} bits \n")
		text.insert(tk.END, f"/{network.cidr()} \n")
		text.insert(tk.END, f"({network.octet()}, {network.increment()}i) \n")
		text.insert(tk.END, f"{'.'.join(map(str, network.subnet()))} \n\n")
		text.insert(tk.END, f"{'.'.join(map(str, network.firstNw()))} \n")
		text.insert(tk.END, f"{network.rangeNw()} \n")
		text.insert(tk.END, f"{'.'.join(map(str, network.broadcast()))} \n")
		text.insert(tk.END, f"{'.'.join(map(str, network.nextNw()))} \n")

	except:
		pass
		

root = tk.Tk()
root.title("Subnet Calculator")
root.geometry("300x420")
root.resizable(width = 'false', height = 'false')
root.configure(background = '#333333')

frame = tk.Frame(root, background = '#333333')
frame.pack()

# for ip address
label_ip = tk.Label(frame, text = "IP address", font = ('Calibri', 12), bg = '#333333', fg = 'white')
label_ip.grid(row = 0, column = 0, columnspan = 3, sticky = 'w')

entry_ip = tk.Entry(frame, font = ('Calibri', 15), justify = 'left', relief = 'flat', width = 25)
entry_ip.focus_set()
entry_ip.grid(row = 1, column = 0, columnspan =3 )

# for hosts
label_host = tk.Label(frame, text = "Hosts", font = ('Calibri', 12), bg = '#333333', fg = 'white')
label_host.grid(row = 2, column = 0, columnspan = 3, sticky = 'w')

entry_host = tk.Entry(frame, font = ('Calibri', 15), justify = 'left', relief = 'flat', width = 25)
entry_host.grid(row = 3, column = 0, columnspan = 3)

# calculate
button = tk.Button(frame, text = "Calculate", command = lambda:calculate(), font = ('Calibri', 12),
					bd = 1, relief = 'ridge', bg = '#262626', fg = 'white', width = 8)
button.grid(row = 4, column = 1, pady = 10)

# result
text = tk.Text(frame, width = 25, height = 10, font = ('Calibri', 15))
text.grid(row = 5, column = 1)


root.mainloop()