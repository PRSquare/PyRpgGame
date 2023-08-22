class DataHolder():
	
	def __init__(self):
		self._data = dict()
		self.test = "test"

	@property
	def data(self):
		return self._data
	
	def add(self, name, value):
		if name in self._data.keys():
			return False
		self._data[name] = value
		return True
	
	def get(self, name): 
		return self._data[name]

MONSTERS = DataHolder()
ITEMS = DataHolder()
LOCATIONS = DataHolder()
