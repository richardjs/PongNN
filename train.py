import pongnn.genetic
import pickle

pool = pongnn.genetic.Pool()
try:
	while True:
		print 'Generation: %d...' % pool.generation
		pool.next_generation()
		print 'Best score:\t%d'  % pool.best_score
except KeyboardInterrupt:
	pickle.dump(pool.best.net, open('best.net', 'w'))
