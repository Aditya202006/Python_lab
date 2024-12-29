class parent():
	def first(self):
		print('first function')
class child(parent):
	def second(self):
		print('second function')
ob = child()
ob.first()
ob.second()


output:
first function
second function
