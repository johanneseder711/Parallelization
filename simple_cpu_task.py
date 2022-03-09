import random 

def append_to_list(lst, num_items, rng=20000000):
	"""
		Function that appends num_items in the range of [0,rng) to the input lst.
	"""
	for n in random.sample(range(rng), num_items):
		lst.append(n)

if __name__ == "__main__":
	# execute the function 2 times
	for i in range(2):
		append_to_list([],10000000)