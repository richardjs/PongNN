import Tkinter as tk
import pongnn
import pickle

root = tk.Tk()
net = pickle.load(open('best.net'))
app = pongnn.app.App(
	root,
	pongnn.player.HumanPlayer(root),
	#pongnn.player.HumanPlayer(root, up_key="'", down_key='/')
	pongnn.player.NeuralPlayer(net)
)
root.mainloop()
