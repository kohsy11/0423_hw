class FourCal:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.add_num = 0
        self.sub_num = 0
        self.mul_num = 0
        self.div_num = 0
    
    def add(self, a, b):
        self.add_num += 1
        return a + b  
    def sub(self, a, b):
        self.sub_num += 1
        return a - b  
    def mul(self, a, b):
        self.mul_num += 1
        return a * b  
    def div(self, a, b):
        if b == 0:
            print("0 inavailable")
            return none
        self.div_num += 1
        return a / b
    def showcount(self):
        print("덧셈: %d" % self.add_num)
        print("뺄셈: %d" % self.sub_num)
        print("곱셉: %d" % self.mul_num)
        print("나눗셈: %d" % self.div_num)


calculator1 = FourCal("고서영", 23, "Korea")
print(calculator1.add(2,3))
print(calculator1.showcount())

