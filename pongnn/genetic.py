import nn
import game
import player
import random

SHAPE = (3, 5, 1)

def play(p1, p2):
	g = game.Game(
		player.NeuralPlayer(p1.net),
		player.NeuralPlayer(p2.net)
	)
	
	while g.ball:
		g.frame()

	assert g.winner.net in (p1.net, p2.net)
	if g.winner.net == p1.net:
		return p1
	else:
		return p2

class Creature(object):
	def __init__(self, net=None):
		if net is None:
			net = nn.NeuralNet(SHAPE)
		self.net = net

class Pool(object):
	SIZE = 40
	TOURNAMENT_SIZE = 5
	CROSSOVER_RATE = .7
	MUTATION_RATE = .001

	def __init__(self):
		self.creatures = [
			Creature() for _ in range(Pool.SIZE)
		]
		self.generation = 0
		self.best = None
		self.best_score = None
		self.new_best = False
	
	def select(self):
		tournament = [
			random.choice(self.creatures) for _ in range(Pool.TOURNAMENT_SIZE)
		]
		
		scores = {entrant: 0 for entrant in tournament}

		for p1 in tournament:
			for p2 in tournament:
				if p1 == p2:
					continue
				winner = play(p1, p2)
				scores[winner] += 1

		best = None
		best_score = None
		for entrant, score in scores.items():
			if score > best_score:
				best = entrant
				best_score = score

		best.score = best_score
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
					random.choice((p2_layer[j], p2_layer[j]))
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
		self.new_best = False
		while len(new_generation) < 40:
			p1 = self.select()
			p2 = self.select()
		
			if p1.score >= self.best_score:
				self.best = p1
				self.best_score = p1.score
				self.new_best = True
			if p2.score >= self.best_score:
				self.best = p2
				self.best_score = p2.score
				self.new_best = True

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

