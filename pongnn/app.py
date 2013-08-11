import Tkinter as tk 
import game

class GameView(tk.Canvas):
	def __init__(self, master, game):
		tk.Canvas.__init__(
			self, master,
			width=game.FIELD_WIDTH, height=game.FIELD_HEIGHT,
			background='#003', highlightthickness=0
		)

class App(object):
	def __init__(self, master):
		master.title('PongNN v.1a')
		master.resizable(0,0)
		
		self.game = game.Game(game.Player(), game.Player())
		self.gameView = GameView(master, self.game)
		self.gameView.grid()
		
		'''
		self.canvas.create_rectangle(50, 50, 60, 100, fill='#633')
		self.canvas.create_rectangle(300, 50, 310, 100, fill='#363')
		'''
