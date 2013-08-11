import random

class Player(object):
	pass

class Paddle(object):
	HEIGHT = 50
	WIDTH = 10
	MARGIN = 25
	LEFT, RIGHT = range(2)

	def __init__(self, game, player, side):
		assert side in (Paddle.LEFT, Paddle.RIGHT)
		
		self.game = game

		self.player = player
		self.side = side

		if side == Paddle.LEFT:
			self.x = Paddle.MARGIN
		else:
			self.x = Game.FIELD_WIDTH - Paddle.MARGIN
		self.y = Game.FIELD_HEIGHT / 2


class Ball(object):
	WIDTH = 7 
	HEIGHT = 7
	SPEED_X = 1
	SPEED_Y = 1

	def __init__(self, game):
		self.game = game
		
		self.x = Game.FIELD_WIDTH / 2
		self.y = Game.FIELD_HEIGHT / 2

		self.dx = Ball.SPEED_X
		if random.randrange(2):
			self.dx *= -1
		self.dy = Ball.SPEED_Y
		if random.randrange(2):
			self.dy *= -1
	
	def frame(self):
		self.x += self.dx
		self.y += self.dy 

		#TODO: Paddle collision - here or in paddle frame?
		

class Game(object):
	FIELD_WIDTH = 500
	FIELD_HEIGHT = 300

	def __init__(self, player1, player2):
		self.paddles = (
			Paddle(self, player1, Paddle.LEFT),
			Paddle(self, player2, Paddle.RIGHT)
		)
		
		self.ball = Ball(self)
	
	def frame(self):
		pass

