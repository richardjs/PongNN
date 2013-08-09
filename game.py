import Tkinter as tk 

class App(object):
	def __init__(self, master):
		master.title('AppNN v.1a')
		master.resizable(0,0)

		self.canvas = tk.Canvas(
			master,
			width=500, height=300,
			background='#003', highlightthickness=0
		)
		self.canvas.grid()

		self.canvas.create_rectangle(50, 50, 60, 100, fill='#633')
		self.canvas.create_rectangle(300, 50, 310, 100, fill='#363')

root = tk.Tk()
app = App(root)
root.mainloop()
