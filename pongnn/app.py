import Tkinter as tk 
import game
import player
import random #Also temporary

class GameView(tk.Canvas):
	def __init__(self, master, game):
		tk.Canvas.__init__(
			self, master,
			width=game.FIELD_WIDTH, height=game.FIELD_HEIGHT,
			background='#003', highlightthickness=0
		)
		
		self.master = master
		self.game = game

		self.paddles = [
			self.create_rectangle(
				*self.__get_rect(paddle),
				fill='#363', width=0 
			) for paddle in game.paddles
		]

		self.ball = self.create_rectangle(
			*self.__get_rect(game.ball),
			fill='#633', width=0
		)

	def run(self, fps=60):
		self.game.frame()
		
		if self.game.ball is None:
			self.game.new_ball()

		for i in range(2):
			self.coords(self.paddles[i], self.__get_rect(self.game.paddles[i]))
		self.coords(self.ball, self.__get_rect(self.game.ball))

		self.master.after(1000 / fps, self.run)

	def __get_rect(self, game_object):
		left = game_object.x - (game_object.WIDTH / 2)
		top = game_object.y - (game_object.HEIGHT / 2)
		return (left, top, left+game_object.WIDTH, top+game_object.HEIGHT)


class App(object):
	def __init__(self, master, player1, player2):
		master.title('PongNN v.1a')
		master.resizable(0,0)
		
		self.game = game.Game(player1, player2)
		self.gameView = GameView(master, self.game)
		self.gameView.grid()

		self.gameView.run()
		
