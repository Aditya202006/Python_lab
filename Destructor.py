class destructor:
	def __init__(self):
		self.greet = "i am PYTHON"
	def display(self):
		print("Hi ",self.greet)
	def __del__(self):
		print("object destroyed")	
dc = destructor()
dc.display()
print(dc)
del dc


output:
Hi  i am PYTHON
<__MAIN__.destructor object at 0x7e656f167dc0>
object destroyed
