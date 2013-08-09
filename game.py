import Tkinter as tk 

class Pong(object):
	def __init__(self, master):
		master.title('PongNN v.1a')
		master.resizable(0,0)

		self.canvas = tk.Canvas(
			master,
			width=500, height=300,
			background='#003', highlightthickness=0
		)
		self.canvas.grid()

root = tk.Tk()
pong = Pong(root)
root.mainloop()
