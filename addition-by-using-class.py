class addition_of_two_numbers:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        return(self.num1+self.num2)

num1=(float(input("enter the first number:-")))
num2=(float(input("enter the second number:-")))
Add_Object=addition_of_two_numbers(num1,num2)
result=Add_Object.addition()
print("the addition of",num1,"and",num2,"is",result)