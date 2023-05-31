#Example_Hybrid_inheritance
class PC:
    def fun1(self):
        print("This is PC class")

class Laptop(PC):
    def fun2(self):
        print("This is Laptop class inheriting PC class")

class Mouse(Laptop):
    def fun3(self):
        print("This is Mouse class inheriting Laptop class")

class Student(Mouse, Laptop):
    def fun4(self):
        print("This is Student class inheriting PC and Laptop")

# Driver’s code
obj = Student()
obj1 = Mouse()
obj.fun4()
obj.fun3()
