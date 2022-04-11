class Calculator:
    def __init__(self, value1, value2): 
        self.value1 = value1
        self.value2 = value2

    def adder(self):
        return self.value1+self.value2  

    def subtractor(self):
        return self.value1 - self.value2

    def multiplier(self):
        return self.value1 * self.value2

    def divider(self):
        return self.value1 / self.value2

    def clear(self):
        self.value1 = 0
        self.value2 = 0
        return self.value1, self.value2


input1 = int(input('Enter 1st number: '))
input2 = int(input('Enter 2nd number: '))

calculatorObj = Calculator(input1, input2)  # creating new calculator object with input1 and input2 values

print("Addition of values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.adder()))
print("Subtraction of values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.subtractor()))
print("Multiplication of values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.multiplier()))
print("Division of values " + str(input1) + " and " + str(input2) + " is " + str(
    calculatorObj.divider()))
print("Clearing values " + str(input1) + " and " + str(input2) + str(
    calculatorObj.clear()))
