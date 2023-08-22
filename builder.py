import random

class Builder():
	def build(self):
		return None

def get_random_index(array):
	if not array:
		return None
	x = random.randrange(0, len(array))
	return x
def get_random_element(array):
	if not array:
		return None
	x = random.randrange(0, len(array))
	return array[x]
