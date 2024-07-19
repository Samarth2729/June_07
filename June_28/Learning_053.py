# Hierarchical Inheritance means
# One father and multiple children

class Father:
    def BHK4(self):
        print('I have BHK4')

class samarth(Father):
    def BHK3(self):
        print('I have BHK3')

class devanshi(Father):
    def BHK2(self):
        print('I have BHK2')

class Pushpak(Father):
    def No_house(self):
        print('I have no house')

Samarth =  samarth()
Samarth.BHK3()
Samarth.BHK4()
print('---------------------------------')
Devanshi = devanshi()
Devanshi.BHK2()
Devanshi.BHK4()
print('---------------------------------')
Pushpak = Pushpak()
Pushpak.No_house()
Pushpak.BHK4()
print('---------------------------------')
