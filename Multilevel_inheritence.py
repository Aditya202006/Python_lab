class parent():
	def first(self):
		print('first function')
class child(parent):
	def second(self):
		print('second function')
class child2(child):
	def third(self):
		print('third function')
ob = child2()
ob.first()
ob.second()
ob.third()

output:
first function
second function
third function
