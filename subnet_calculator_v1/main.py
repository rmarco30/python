import tkinter as tk
import subnet as sn
import math

	
ip = ''
host = ''

def calculate():

	try:
	
		ip = entry1.get()
		host = entry2.get()
		host = int(host, 10)

		bits = sn.bits(host, 'str')
		cidr = sn.cidr(host, 'str')
		incr = sn.increment(host, 'str')
		subn = sn.subnet(host, 'dec')
		fnet = sn.first_nw(ip, 'str')
		nnet = sn.next_nw(ip, host, 'str')
		bcst = sn.broadcast(ip, host, 'str')
		rnge = sn.range_nw(ip, host)

		text.delete(1.0, tk.END)
		text.insert(tk.END, str(bits) + '\n')
		text.insert(tk.END, str(cidr) + '\n')
		text.insert(tk.END, str(incr) + '\n')
		text.insert(tk.END, str(subn) + '\n')
		text.insert(tk.END, str(fnet) + '\n')
		text.insert(tk.END, str(rnge) + '\n')
		text.insert(tk.END, str(bcst) + '\n')
		text.insert(tk.END, str(nnet) + '\n')

	except:
		pass

# def copyall():
# 	pass


root = tk.Tk()
root.title("Subnet Calculator")
root.geometry("300x470")
root.resizable(width = 'false', height = 'false')
root.configure(background = '#333333')

frame = tk.Frame(root, background = '#333333')
frame.pack()


# for ip address
label1 = tk.Label(frame, text="IP address", font=('Calibri', 12), background = '#333333', foreground = 'white')
label1.grid(row=0, column=0, columnspan=3, sticky='w')

entry1 = tk.Entry(frame, font=('Calibri', 15), justify='left', relief = 'flat', width = 25)
entry1.focus_set()
entry1.grid(row=1, column=0, columnspan=3)

# for hosts
label2 = tk.Label(frame, text="Hosts", font=('Calibri', 12), background = '#333333', foreground = 'white')
label2.grid(row=2, column=0, columnspan=3, sticky='w')

entry2 = tk.Entry(frame, font=('Calibri', 15), justify='left', relief = 'flat', width = 25)
entry2.grid(row=3, column=0, columnspan=3)

# calculate
button = tk.Button(frame, text="Calculate", command = lambda: calculate(), font=('Calibri', 12), bd=1, relief='ridge', bg='#262626', fg='white', width=8)
button.grid(row=4, column = 1, pady = 10)

# result
text = tk.Text(frame, width=25, height = 10, font=('Calibri', 15))
text.grid(row=5, column=1)

# select all and copy
# button = tk.Button(frame, text="Copy All", command = lambda: copyall(), font=('Calibri', 12), bd=1, relief='ridge', bg='#262626', fg='white', width=8)
# button.grid(row=6, column = 1, pady = 10)

root.mainloop()