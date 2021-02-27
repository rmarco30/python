import tkinter as tk
from sci_cal import SciCal

def main():

	root = tk.Tk()
	root.title("Sientific Calculator")
	# root.wm_iconbitmap('C:\\Users\\Marco\\Project Files\\Python\\sci_cal_py\\images\\calc.ico')
	root.geometry("300x470")
	root.resizable(width = 'false', height = 'false')
	root.configure(background = '#333333')

	calc = SciCal(root)

	root.mainloop()

if __name__ == '__main__':

	main()