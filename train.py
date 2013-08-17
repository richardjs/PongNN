import pongnn.genetic
import pickle

pool = pongnn.genetic.Pool()
try:
	while True:
		print 'Generation %d...' % pool.generation
		pool.next_generation()
		print 'Best score:\t%d'  % pool.best_score

		total = 0
		for creature in pool.creatures:
			total += creature.score
		avg = 1.0 * total / len(pool.creatures)
		print 'Average score:\t%f' % avg  

except KeyboardInterrupt:
	pickle.dump(pool.best.net, open('best.net', 'w'))
