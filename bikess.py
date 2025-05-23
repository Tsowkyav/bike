'''print(50+4)
a=int(input ("enter a number:"))
if a %2==0:
    print("number is even")
else:
    print("number is odd")'''
'''age=int(input("enter a number"))
if age >=18:
    print("eligible")
else:
    print("not eligible ")
num=int(input("enter a number:"))
if num%7==0:
    print("the number is divisival by seven")
elif num%7>0:
    print("not divisile by seven")
else:
    print("not")'''
class bike1():
    def person1(self, button):
        self. button= button
        print(" i pressed first button")
        if button==100:
            print("bike1 moved")
        else:
                print("go to 2 bike")
class bike2():
    def person2(self,button):
        self.button=button
        print("i pressed second button")
        if button==2:
            print("bike 2 is moved")
class bike3():
    def person3(self,button):
        super().__init__()
        print("i pressed 3 button")
        if button==1:
            print("person1 moved")
        elif button==2:
            print("person2 moved")
        else:
            print("person 3  moved")
a=bike1()
a.person1(5)
b=bike2()
b.person2(100)
c=bike3()
c.person3(12)
