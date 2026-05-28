class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return int(a/b)


calculator = Calculator()

print(calculator.add(5 , 5))
print(calculator.sub(20 , 10))
print(calculator.mul(2 , 5))
print(calculator.div(100, 10 ))

