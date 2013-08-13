import math
import random

class Neuron(object):
	def __init__(self, inputs, weights=None):
		assert None in (inputs, weights) or len(inputs)+1 == len(weights)
		self.inputs = inputs

		if weights is None and inputs is not None:
			weights = [
				random.uniform(-1, 1) for _ in range(len(inputs)+1)
			]
		self.weights = weights
	
	@property
	def activation(self):
		assert self.weights is not None
		total = 0
		for i in range(len(self.inputs)):
			total += self.inputs[i].activation * self.weights[i]
		total += self.weights[-1]
		
		try:
			return ( 2 / (1 + math.e**(-total)) ) - 1
		except OverflowError:
			return 0


class InputNeuron(Neuron):
	def __init__(self):
		Neuron.__init__(self, None)

	@property
	def activation(self):
		assert hasattr(self, 'value')
		return self.value


class NeuralNet(object):
	def __init__(self, shape, weights=None):
		assert len(shape) >= 2
		self.layers = []
		self.layers.append(
			[InputNeuron() for _ in range(shape[0])]
		)
		for count in shape[1:]:
			self.layers.append(
				[Neuron(self.layers[-1]) for _ in range(count)]
			)

		if weights is not None:
			self.weights = weights

	@property
	def weights(self):
		return [
			[neuron.weights for neuron in layer] for layer in self.layers[1:]
		]
	
	@weights.setter
	def weights(self, weights):
		assert len(weights) == len(self.layers)-1
		for i in range(len(self.layers[1:])):
			layer = self.layers[i+1]
			layer_weights = weights[i]
			assert len(layer_weights) == len(layer)
			for j in range(len(layer)):
				assert len(layer_weights[j]) == len(self.layers[i])+1
				layer[j].weights = layer_weights[j]
	
	def think(self, inputs):
		assert len(inputs) == len(self.layers[0])
		for i in range(len(inputs)):
			self.layers[0][i].value = inputs[i]

		return [
			neuron.activation for neuron in self.layers[-1] 
		]
