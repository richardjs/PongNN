import nn
import game
import player
import random

SHAPE = (3, 4, 1)

class Creature(object):
	def __init__(self, net=None):
		if net is None:
			net = nn.NeuralNet(SHAPE)
		self.net = net

		self._score = None
	
	@property
	def score(self):
		if self._score is not None:
			return self._score

		g = game.Game(
			player.NeuralPlayer(self.net),
			player.NeuralPlayer(self.net)
		)
		
		while g.ball and g.ball.bounces < 100:
			g.frame()
		
		if g.last_ball is not None:
			ball = g.last_ball
		else:
			ball = g.ball


		if ball.x < g.FIELD_WIDTH/2:
			paddle = g.paddles[0]
		else:
			paddle = g.paddles[1]
		dist = 1 - (1.0 * abs(ball.y - paddle.y) / g.FIELD_HEIGHT)

		self._score = g.last_ball.bounces + dist
		return self._score

class Pool(object):
	SIZE = 40 
	TOURNAMENT_SIZE = 5 
	CROSSOVER_RATE = .7
	MUTATION_RATE = .05

	def __init__(self):
		self.creatures = [
			Creature() for _ in range(Pool.SIZE)
		]
		self.generation = 0
		self.best = None
		self.best_score = None
	
	def select(self):
		tournament = [
			random.choice(self.creatures) for _ in range(Pool.TOURNAMENT_SIZE)
		]
		
		best = None
		best_score = None
		for entrant in tournament:
			if entrant.score > best_score:
				best = entrant
				best_score = entrant.score

		return best
	
	def crossover(self, p1, p2):
		p1_weights = p1.net.weights
		p2_weights = p2.net.weights
	
		child_weights = []
		for i in range(len(p1_weights)):
			p1_layer = p1_weights[i]
			p2_layer = p2_weights[i]
			child_layer = []
			for j in range(len(p1_layer)):
				child_layer.append(
					list(random.choice((p1_layer[j], p2_layer[j])))
				)
			child_weights.append(child_layer)
		
		return Creature(
			nn.NeuralNet(SHAPE, weights=child_weights)
		)

	def mutate(self, child):
		child_weights = child.net.weights
		for i in range(len(child_weights)):
			for j in range(len(child_weights[i])):
				for k in range(len(child_weights[i][j])):
					if random.random() < Pool.MUTATION_RATE:
						child_weights[i][j][k] += random.uniform(-1, 1)
		child.net.weights = child_weights

	def next_generation(self):
		new_generation = []
		if self.best is not None:
			new_generation.append(self.best)

		while len(new_generation) < Pool.SIZE:
			p1 = self.select()
			p2 = self.select()

			if random.random() < Pool.CROSSOVER_RATE:
				c1 = self.crossover(p1, p2)
				c2 = self.crossover(p1, p2)
				self.mutate(c1)
				self.mutate(c2)
				new_generation.append(c1)
				new_generation.append(c2)
			else:
				new_generation.append(p1)
				new_generation.append(p2)
		
		self.creatures = new_generation
		self.generation += 1

		for creature in self.creatures:
			if creature.score > self.best_score:
				self.best = creature
				self.best_score = creature.score

