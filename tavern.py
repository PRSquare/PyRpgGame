import player # quest
import globaldata
import builder

class Tavern():
	def __init__(self):
		self.available_quests = []
		self.questsAmount = 2
	def gen_quests(self, location, rewards):
		self.available_quests.clear()
		for i in range(0, self.questsAmount):
			self.available_quests.append(self._gen_quest(location, rewards[i]))
	def _gen_quest(self, location, reward):
		q = player.Quest()
		q.reward = reward
		taget = builder.get_random_element(globaldata.ITEMS.data).build()
		q.taget = taget
		taget.isProtected = True
		q.name = f"Search of {taget.name}"
		q.description = f"Find a {taget.name} somwere in {location.name}, and you will get {q.reward.name}"
		return q

	def get_quest(self, quest):
		self.available_quests.remove(quest)
		return quest

	def get_quest_by_id(self, qid):
		return self.available_quests.pop(qid)