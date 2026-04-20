class Calculator:
    def add(self,num1,num2):
        print(num1+num2)

    def div(self,num1,num2):
        try:
            print("resource open")
            print(num1/num2)
        except ZeroDivisionError as e:
            print(e)
        except TypeError as e:
            print(e)
        finally:
            #code will run in both the cases either exception raised or not
            print("resource closed")

c1 = Calculator()
c1.add(10,12)
c1.div('p',0)



