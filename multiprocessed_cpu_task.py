import random 
import multiprocessing

NUM_PROC = 2

def append_to_list(lst, num_items, rng=20000000):
	"""
		Function that appends num_items in the range of [0,rng) to the input lst.
	"""
	for n in random.sample(range(rng), num_items):
		lst.append(n)

if __name__ == "__main__":

	jobs=[]

	for i in range(NUM_PROC):
		process = multiprocessing.Process(
				target=append_to_list,
				args=([],10000000)
			)
		jobs.append(process)

	for j in jobs:
		j.start()
	for j in jobs:
		j.join()