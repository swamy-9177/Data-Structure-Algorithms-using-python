class Student:
    def __init__(self,roll,sec):
        self.roll=roll
        self.sec=sec
    def study(self):
        print("i study and my roll is ",self.roll)
rahul=Student(12,"a")
rahul.study()
