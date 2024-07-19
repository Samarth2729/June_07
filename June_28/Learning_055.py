# Multiple imheritance

class Father:

    def fiftythousand(self):
        print('I have 50 thousand')

class Mother:

    def onelac(self):
        print('I have one lac')

class Son(Father, Mother):

    def Berojgar(self):
        print('I am berojgar')

child = Son()
child.fiftythousand()
child.onelac()
child.Berojgar()
print('---------------------------------')
