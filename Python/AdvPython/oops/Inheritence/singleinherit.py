class Bank(object):
	cash = 10000000
	def available_cash(self):
		print(self.cash)

class canarabank(Bank):
    pass
class statebank(Bank):
	cash = 20000000
	def available_cash(self):
		print(self.cash+Bank.cash)

c = canarabank()
c.available_cash()
s = statebank()
s.available_cash()
