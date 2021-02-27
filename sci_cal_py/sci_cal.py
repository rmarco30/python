import tkinter as tk
import sympy as sp
from chars import chars



class SciCal:

	def __init__(self, master):

		frame = tk.Frame(master, bg = '#333333')
		frame.pack()

		# variables
		self.equation = ''
		self.equation_dec = ''
		self.expression = ''
		self.ans = ''
		self.x = sp.Symbol('x')
		self.error = False
		self.gotcha = False
		self.s = True


		# entry widget
		self.entry = tk.Entry(frame, width=16, font=('Calibri', 25), justify='right', relief = 'flat', insertbackground='white')
		self.entry.focus_set()
		self.entry.bind('<Key>', self.pressed)
		self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15)
		

		# buttons with different calling functions
		self.delBtn = self.create_buttons_2(frame, 'DEL', lambda: self.delete(), '#262626', 1, 0)
		self.clrBtn = self.create_buttons_2(frame, 'CLR', lambda: self.clear(), '#262626', 1, 1)
		self.sigBtn = self.create_buttons_2(frame, '+/-', lambda: self.sign(), '#262626', 5, 0)
		self.piBtn = self.create_buttons_2(frame, 'S ↔ D', lambda: self.stdToDec(), '#262626', 8, 3)
		self.ansBtn = self.create_buttons_2(frame, 'ANS', lambda: self.answer(), '#262626', 9, 3)
		self.eqlBtn = self.create_buttons_2(frame, 'solve', lambda: self.shiftSolve(), '#262626', 10, 3)
		self.binBtn = self.create_buttons_2(frame, 'BIN', lambda: self.toBin(), '#333333', 11, 0)
		self.hexBtn = self.create_buttons_2(frame, 'HEX', lambda: self.toHex(), '#333333', 11, 1)
		self.decBtn = self.create_buttons_2(frame, 'DEC', lambda: self.toDec(), '#333333', 11, 2)
		self.eqlBtn = self.create_buttons_2(frame, '=', lambda: self.solve(), '#009999', 11, 3)


		# create and arrange buttons with the same calling functions
		self.row = 1
		self.col = 2

		for k, v in chars.items():

			# if statements for skipping a grid when arranging buttons
			if self.row == 5 and self.col == 0:
				self.col = 1

			if self.row == 8 and self.col == 3:
				self.row = 9
				self.col = 0

			if self.row == 9 and self.col == 3:
				self.row = 10
				self.col = 0

			button = self.create_buttons_1(frame, k, v, self.row, self.col)

			self.col += 1

			if self.col == 4:
				self.row += 1
				self.col = 0


	# function when button is clicked
	def clicked(self, num):

		if self.error == True:
			self.update()
			self.error = False

		if self.gotcha == True:
			self.entry.delete(0, tk.END)
			self.gotcha = False

		self.entry.insert(tk.END, num)
		self.equation = self.entry.get()


	# function when keyboard keys are pressed
	def pressed(self, event):

		if self.error == True:
			self.update()
			self.error = False

		if event.char == '\b':
			self.delete()

		else:
			self.p = str(event.char)
			self.equation = str(self.equation) + self.p

		if event.char == '\r':
			self.solve()


	# function for updating screen
	def update(self):

		self.entry.delete(0, tk.END)
		self.entry.insert(tk.END, self.equation)


	# clear screen and equation variable
	def clear(self):
		self.entry.delete(0, tk.END)
		self.equation = ''
		self.equation_dec = ''
		self.ans = ''


	# delete last character input
	def delete(self):

		self.update()
		self.equation = str(self.equation)
		self.equation = self.equation[:-1]

		if self.equation:
			self.update()
		else:
			self.entry.delete(0, tk.END)


	# function that will handle the calculation
	def solve(self):

		try:
			self.equation_cpy = self.equation
			self.equation = sp.sympify(self.equation)
			self.equation_dec = sp.N(self.equation, 6)
			self.ans = self.equation

			if str(self.equation) == 'zoo':
				self.entry.delete(0, tk.END)
				self.entry.insert(tk.END, 'Division by Zero')
				self.equation = self.equation_cpy
				self.error = True

			else:
				self.entry.delete(0, tk.END)
				self.entry.insert(tk.END, str(self.equation))
				self.gotcha = True
					
		except:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, 'SyntaxError')
			self.error = True


	# function for solving simple linear algebra
	def shiftSolve(self):

		try:
			self.lhs = self.equation.split('=')[0]
			self.rhs = self.equation.split('=')[-1]
			self.lhs = sp.sympify(self.lhs)
			self.transpose = '(-1)*' + '(' + str(self.lhs) + ')'
			self.transpose = sp.sympify(self.transpose)
			self.expression = self.rhs + '+' + str(self.transpose)
			self.expression = sp.solve(self.expression, self.x)
			self.expression = 'x = ' + str(self.expression[0])
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, self.expression)
			self.ans = self.expression.split('=')[-1]
			self.gotcha = True

		except:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, 'SyntaxError')
			self.error = True


	# show value from the previous calculation
	def answer(self):

		self.entry.insert(tk.END, str(self.ans))
		self.equation = str(self.equation) + str(self.ans)


	# convert input to binary
	def toBin(self):

		self.equation = str(self.equation)
		
		try:
			if 'b' in self.equation:
				pass

			elif 'x' in self.equation:
				self.equation = bin(int(self.equation, 16))
				self.update()

			else:
				self.equation = bin(int(self.equation, 10))
				self.update()

		except:
				self.entry.delete(0, tk.END)
				self.entry.insert(tk.END, 'SyntaxError')
				self.error = True


	# convert input to hexadecimal
	def toHex(self):

		self.equation = str(self.equation)

		try:
			if 'x' in self.equation:
				pass

			elif 'b' in self.equation:
				self.equation = hex(int(self.equation, 2))
				self.update()

			else:
				self.equation = hex(int(self.equation, 10))
				self.update()

		except:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, 'SyntaxError')
			self.error = True


	# convert input to decimal
	def toDec(self):

		try:
			self.equation = sp.sympify(self.equation)
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, self.equation)

		except:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, 'ValueError')
			self.error = True


	# function for toggling between standard to decimal
	def stdToDec(self):

		if self.s:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, self.equation_dec)
			self.s = False

		else:
			self.entry.delete(0, tk.END)
			self.entry.insert(tk.END, self.equation)
			self.s = True


	# function for inserting / deleting a sign. it basically toggles between positive and negative
	def sign(self):

		if len(self.equation) == 0:
			self.clicked('-')

		elif self.equation[-1] == '-':
			self.equation = self.equation[:-1]
			self.update()

		else:
			self.clicked('-')


	# for creating a button with same functions as its symbol (0-9, parentheses, MDAS, etc...)
	def create_buttons_1(self, master, k, v, row, column):

		return tk.Button(master, text=k, command=lambda: self.clicked(v), font=('Calibri', 12), bd=1, relief='ridge', bg='#262626', fg='white', width=8).grid(row=row, column=column)


	# for creating button with special functions (clear, del, binary, etc...)
	def create_buttons_2(self, master, text, command, bg, row, column):

		return tk.Button(master, text=text, command=command, font=('Calibri', 12), bd=1, relief='ridge', bg=bg, fg='white', width=8).grid(row=row, column=column)