class Transport:
    ClassName = "Транспорт"
    objCount = 0
    def __init__(self, color, year, type):
        self.color = color
        self.year = year
        self.type = type
        self.age = self.count_age()
        Transport.objCount += 1
    def stop(self):
        print("Нажата педаль тормоза!")
        
    def drive(self):
        print("Нажата педаль газа!")
    
    def count_age(self):
        return 2022 - self.year

    def info(self):
        print(self.age,self.year,self.color,self.type)

auto1 = 0
print(id(auto1))
auto1 = Transport('red', 2009, 'light')
auto2 = Transport('green', 1991, 'truck')
auto1.drive()
auto1.stop()
auto2.info()
print(auto1.ClassName,auto2.ClassName)
print(Transport.objCount)
pass