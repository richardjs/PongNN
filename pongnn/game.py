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

