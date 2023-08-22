class Effect():
	def __init__(self, target = None, caster = None):
		self._name = "Unnamed Effect"
		self._description = "Effect unknown"
		self._isApplied = False
		self._isActive = True
		self._duration = 1
		self._inic_duration = self._duration
		self._delay = 0
		self._inic_delay = self._delay
		self._target = target
		self._caster = caster
		self._isResetable = False

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, val):
		if val != None:
			self._name = val

	@property
	def description(self):
		return self._description
	@description.setter
	def description(self, val):
		if val != None:
			self._description = val
			

	@property
	def duration(self):
		return self._duration
	@duration.setter
	def duration(self, d):
		if d != None:
			self._duration = d
			self._inic_duration = d	
	@property
	def delay(self):
		return self._delay
	@delay.setter
	def delay(self, d):
		if d != None:
			self._delay = d
			self._inic_delay = d

	@property
	def target(self):
		return self._target
	@target.setter
	def target(self, t):
		if self._target == None or self._duration <= 0:
			self._target = t

	@property
	def caster(self):
		return self._caster
	@caster.setter
	def caster(self, c):
		if self._target == None or self._duration <= 0:
			self.caster = t

	@property 
	def isApplied(self):
		return self._isApplied
	@property 
	def isActive(self):
		return self._isActive
	
	@property
	def isResetable(self):
		return self._isResetable
	@isResetable.setter
	def isResetable(self, val):
		if val != None:
			self._isResetable = val

	def reset(self):
		# self.target = None
		# self.caster = None
		if not self.isResetable:
			return
		self._isApplied = False
		self._isActive = True
		self._duration = self._inic_duration
		self._delay = self._inic_delay

	def update(self):
		if not self._isActive:
			return
		if self._delay > 0:
			self._delay -= 1
			return

		if not self._isApplied:
			self.on_apply()
			self._isApplied = True
			return

		while self._duration > 0 or self._duration == -1: # -1 for constant effect
			self.on_tick()
			if self._duration != -1:
				self._duration -= 1
			return

		self.on_end()
		self._isActive = False

	def on_apply(self):
		pass

	def on_tick(self):
		pass

	def on_end(self):
		pass