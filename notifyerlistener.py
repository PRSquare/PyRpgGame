class Listener():
	target = None
	isActive = True
	def target_fits(self, target):
		return self.target == target
	def on_notify(self):
		pass

class Notifyer():
	listeners = []

	def notify(self, target):
		print(target)
		# for l in self.listeners:
		# 	if l.target_fits(target):
		# 		l.on_notify()
		# self._update_listeners()

	def add_listener(self, listener):
		if not listener in self.listeners:
			self.listeners.append(listener)
	def remove_listener(self, listener):
		self.listener.remove(listener)

	def clear_listeners(self):
		self.listeners.clear()

	def _update_listeners(self):
		for l in self.listeners:
			if not l.isActive:
				self.remove_listener(l)
