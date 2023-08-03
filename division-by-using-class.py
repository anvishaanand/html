class division:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def divide(self):
        return(self.num1/self.num2)

num1=(float(input("enter the first number:-")))
num2=(float(input("enter the second number")))
division_object=division(num1,num2)
result=division_object.divide()
print("the division of two numbers is",result)