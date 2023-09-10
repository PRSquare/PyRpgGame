import notifyerlistener

class Quest(notifyerlistener.Listener):
	isComplited = False
	isRuined = False
	name = "quest"
	description = "no description"
	questType = None

	target = None
	amount = 0

	reward = None # Item

	def __init__(self):
		self.reward = builder.get_random_element(globaldata.ITEMS.data).build()

	def on_notify(self, val):
		if val != target:
			return
		if self.amount > 0:
			self.amount -= 1
			return

		isComplited = True