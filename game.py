import Tkinter as tk 

class Player(object):
	pass

class Paddle(object):
	LENGTH = 50
	WIDTH = 10
	MARGIN = 25
	LEFT, RIGHT = range(2)
	def __init__(self, player, side):
		assert side in (Paddle.LEFT, Paddle.RIGHT)

		self.player = player
		self.side = side

		if side == Paddle.LEFT:
			self.x = Paddle.MARGIN
		else:
			self.x = Game.FIELD_WIDTH - Paddle.MARGIN
		self.y = Game.FIELD_HEIGHT / 2

class Game(object):
	FIELD_WIDTH = 500
	FIELD_HEIGHT = 300
	def __init__(self, player1, player2):
		self.paddles = (
			Paddle(player1, Paddle.LEFT),
			Paddle(player2, Paddle.RIGHT)
		)

class GameView(tk.Canvas):
	def __init__(self, master, game):
		tk.Canvas.__init__(
			self, master,
			width=Game.FIELD_WIDTH, height=Game.FIELD_HEIGHT,
			background='#003', highlightthickness=0
		)

class App(object):
	def __init__(self, master):
		master.title('PongNN v.1a')
		master.resizable(0,0)
		
		self.game = Game(Player(), Player())
		self.gameView = GameView(master, self.game)
		self.gameView.grid()
		
		'''
		self.canvas.create_rectangle(50, 50, 60, 100, fill='#633')
		self.canvas.create_rectangle(300, 50, 310, 100, fill='#363')
		'''

root = tk.Tk()
app = App(root)
root.mainloop()
