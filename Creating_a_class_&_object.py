class student:
	branch = 'CSE'
	def read_student_details(self,rno,n):
		self.regdno = rno
		self.name = n
	def print_student_details(self):
		print("Student regdn.no is",self.regdno)
		print("Student name is", self.name)
		print("Student branch is",student.branch)
s=student()
s.read_student_details("23PA1A05__","Aditya")
s.print_student_details()

output:
Student regdn.no is 23PA1A05__
Student name is Aditya
Student branch is CSE
