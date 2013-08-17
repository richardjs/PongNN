import random

class Paddle(object):
	HEIGHT = 50
	WIDTH = 10
	MARGIN = 25
	SPEED = 5

	LEFT, RIGHT = range(2)

	def __init__(self, game, player, side):
		assert side in (Paddle.LEFT, Paddle.RIGHT)
		
		player.paddle = self
		
		self.game = game
		self.player = player
		self.side = side

		if side == Paddle.LEFT:
			self.x = Paddle.MARGIN
		else:
			self.x = Game.FIELD_WIDTH - Paddle.MARGIN
		self.y = Game.FIELD_HEIGHT / 2

	def frame(self):
		move = self.player.get_move()
		
		if move == self.player.NO_MOVE:
			return
		elif move == self.player.MOVE_UP:
			self.y -= Paddle.SPEED
		else:
			self.y += Paddle.SPEED
		
		half_height = Paddle.HEIGHT / 2
		if self.y - half_height < 0:
			self.y = half_height
		elif self.y + half_height > Game.FIELD_HEIGHT:
			self.y = Game.FIELD_HEIGHT - half_height


class Ball(object):
	WIDTH = 7 
	HEIGHT = 7
	SPEED_X = 1 
	SPEED_Y = 1.5 

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

		self.bounces = 0
	
	def frame(self):
		self.x += self.dx
		self.y += self.dy 

		left = self.x - Ball.WIDTH/2
		right = self.x + Ball.WIDTH/2
		top = self.y - Ball.HEIGHT/2
		bottom = self.y + Ball.HEIGHT/2

		if (top < 0 or bottom > Game.FIELD_HEIGHT):
			self.dy *= -1

		if (right < 0 or left > Game.FIELD_WIDTH):
			self.game.ball_out()
		
		for paddle in self.game.paddles:
			if abs(self.x - paddle.x) * 2 < Ball.WIDTH + Paddle.WIDTH:
				if abs(self.y - paddle.y) * 2 < Ball.HEIGHT + Paddle.HEIGHT:
					if paddle.side == Paddle.LEFT:
						self.dx = abs(self.dx)
						self.x = paddle.x + Paddle.WIDTH/2 + Ball.WIDTH/2
					else:
						self.dx = - abs(self.dx)
						self.x = paddle.x - Paddle.WIDTH/2 - Ball.WIDTH/2
					self.bounces += 1
					print self.bounces

class Game(object):
	FIELD_WIDTH = 500
	FIELD_HEIGHT = 300

	def __init__(self, player1, player2):
		player1.game = self
		player2.game = self

		self.paddles = (
			Paddle(self, player1, Paddle.LEFT),
			Paddle(self, player2, Paddle.RIGHT)
		)

		self.ball = Ball(self)
		self.last_ball = None
	
	def frame(self):
		for paddle in self.paddles:
			paddle.frame()

		self.ball.frame()
	
	def ball_out(self):
		assert self.ball.x < 0 or self.ball.x > Game.FIELD_WIDTH
		if self.ball.x < 0:
			self.winner = self.paddles[Paddle.RIGHT].player
		else:
			self.winner = self.paddles[Paddle.LEFT].player
		
		self.last_ball = self.ball
		self.ball = None
	
	def new_ball(self):
		self.ball = Ball(self)
