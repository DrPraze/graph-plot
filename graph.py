from tkinter.messagebox import showerror
import matplotlib.pyplot as plt
import numpy as np 
from pandas import DataFrame
from matplotlib.widgets import TextBox

class Graph:
	def __init__(self):
		x = np.linspace(-5, 5, 100)
		y = 5*x**2-2*x**5/7-2**3*x
		plt.plot(x, y, '-r', label = None)
		plt.title('Graph Plot')
		plt.xlabel('X', color = '#1C2833')
		plt.ylabel('Y', color = '#1C2833')
		self.text()

	def text(self):
		axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
		text_box = TextBox(axbox, 'Enter Equation')
		text_box.on_submit(self.submit)
		plt.show()

	def submit(self, text):
		try:
			x = np.linspace(-5, 5, 100)
			y = eval(text)
			plt.close()

			plt.plot(x, y, '-r', label = None)
			plt.title('Graph Plot')
			plt.xlabel('X', color = '#1C2833')
			plt.ylabel('Y', color = '#1C2833')
			#plt.legend(loc = 'upper left')
			self.text()
			plt.grid()
			plt.show()
		except Exception as e:
			showerror('An error occured', e)
	
if __name__=='__main__':
	Graph()
