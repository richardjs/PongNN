class Player(object):
	MOVE_UP, MOVE_DOWN, NO_MOVE = range(3)
	
	def get_move(self):
		raise 'Please implement!'


class HumanPlayer(Player):
	def __init__(self, root, up_key='a', down_key='z'):
		root.bind('<%s>' % up_key, self.up_key_pressed)
		root.bind('<KeyRelease-%s>' % up_key, self.up_key_released)
		root.bind('<%s>' % down_key, self.down_key_pressed)
		root.bind('<KeyRelease-%s>' % down_key, self.down_key_released)

		self.up_on = False
		self.down_on = False
	
	def up_key_pressed(self, event):
		self.up_on = True

	def up_key_released(self, event):
		self.up_on = False
	
	def down_key_pressed(self, event):
		self.down_on = True
	
	def down_key_released(self, event):
		self.down_on = False
	
	def get_move(self):
		if self.up_on == self.down_on:
			return Player.NO_MOVE
		
		if self.up_on:
			return Player.MOVE_UP
		return Player.MOVE_DOWN

class PerfectAIPlayer(Player):
	def get_move(self):
		if self.paddle.y + self.paddle.HEIGHT/4 < self.game.ball.y:
			return Player.MOVE_DOWN
		elif self.paddle.y - self.paddle.HEIGHT/4 > self.game.ball.y:
			return Player.MOVE_UP
		else:
			return Player.NO_MOVE
