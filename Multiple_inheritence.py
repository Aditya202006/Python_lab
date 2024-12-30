class parentA:
    def first(self):
        print('First function from parentA')

class parentB:
    def second(self):
        print('Second function from parentB')

class parentC:
    def third(self):
        print('Third function from parentC')

class child(parentA, parentB, parentC):
    def fourth(self):
        print('Fourth function from child')

ob = child()
ob.first()
ob.second()
ob.third()   
ob.fourth()  

'''
output:
First function from parentA
Second function from parentB
Third function from parentC
Fourth function from child
'''
