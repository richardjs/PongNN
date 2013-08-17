import Tkinter as tk
import pongnn
import pickle

root = tk.Tk()
net1 = pickle.load(open('best.net'))
net2 = pickle.load(open('best.net'))
app = pongnn.app.App(
	root,
	#pongnn.player.HumanPlayer(root),
	#pongnn.player.HumanPlayer(root, up_key="'", down_key='/')
	pongnn.player.NeuralPlayer(net1),
	pongnn.player.NeuralPlayer(net2)
)
root.mainloop()
