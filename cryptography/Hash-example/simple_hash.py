import random
import time

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def create_simple_hash(length :int):
	"""docstring for create_simple_hash:
:	create_simple_hash needs an integer as an input and will return a "random" Hash with the length of the given integer."""

	simple_hash = ''
	for i in range(length):
		if random.randint(0, 9999) % 3 == 0:
			simple_hash += str(random.randint(0, 9))
		else:
			if random.randint(0, 9999) % 2 == 0:
				simple_hash += str(alphabet[random.randint(0, len(alphabet)-1)])
			else:
				simple_hash += str(alphabet[random.randint(0, len(alphabet)-1)].lower())
	return simple_hash

def create_simple_hash_with_difficulty(hash_length:int, difficulty:int):
	"""docstring for create_simple_hash_with_difficulty:
	create_simple_hash_with_difficulty needs two integers. The first one sets the length of the Hash and the second one \
	sets the difficulty for the Hash computations. create_simple_hash_with_difficulty returns the computed Hash and its computation-time."""

	start_time = time.time()
	check = True
	while check:
		test = create_simple_hash(hash_length)
		test_count = 0
		for i in range(0, difficulty):
			if (test[i].lower() and test[i].upper()) not in alphabet and int(test[i]) == 0: test_count += 1
		if test_count == difficulty: check = False
	end_time = time.time()

	return test, round(end_time - start_time, 5)

alphabet2 = ["A", "B", "C", "D", "E", "F"]

def create_simple_ETHaddress(length :int):
	"""docstring for create_simple_hash:
	create_simple_hash needs an integer as an input and will return a "random" Hash with the length of the given integer."""

	simple_ETH_address = ''
	for i in range(length):
		if random.randint(0, 99999) % 3 == 0:
			simple_ETH_address += str(random.randint(0, 9))
		else:
			if random.randint(0, 99999) % 9 == 0:
				simple_ETH_address += str(alphabet2[random.randint(0, len(alphabet2)-1)])
			else:
				simple_ETH_address += str(alphabet2[random.randint(0, len(alphabet2)-1)].lower())
	#if any(letter in simple_ETH_address for letter in alphabet2): return simple_ETH_address 
	#else: return create_ETHaddress(length)
	return simple_ETH_address
