class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # swap b and a

    def multiply(self, a, b):
        result = 0
        flag = 1 if(b < 0) else 0 # create flag
        if(flag):
            b = 0 - b
        for i in range(b): # change b+1 to b
            if(flag): # create codition handle case b < 0
                result = self.subtract(result, a)
            else:
                result = self.add(result, a)

        return result

    def divide(self, a, b):
        result = 0
        while a > b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while a <= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))