class Bird:
    def  __init__(self, name):
        self.name = name
    def hello(self):
        print('Я птица', self.name)

b1 = Bird('Geht')
b2 = Bird('Lovisan')

b1.hello()
b2.hello()