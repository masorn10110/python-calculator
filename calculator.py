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
        if(b == 0): # handle case divide by 0
            return ZeroDivisionError
        result = 0
        flag1 = 1 if(b < 0) else 0 # create flag
        flag2 = 1 if(a < 0) else 0 # create flag
        if(flag1):
            b = 0 - b
        if(flag2):
            a = 0 - a
        while a >= b: # change > to >=
            a = self.subtract(a, b)
            result += 1
        if(flag1): # inverse value that should be negative
            result = 0 - result
        if(flag2):
            result = 0 - result
        return result
    
    def modulo(self, a, b):
        if(b == 0): # handle case divide by 0
            return ZeroDivisionError
        flag1 = 1 if(b < 0) else 0 # create flag
        flag2 = 1 if(a < 0) else 0 # create flag
        while 1: # add more condition to handle all case
            if(flag1 == flag2): # case have same sign
                a = a-b
                if(flag1 and a > b):
                    return a
                if((not flag1) and a < b):
                    return a
            else: # case have different sign
                a = a+b
                if(flag1 and a < b):
                    return a - b
                if((not flag1) and a > b):
                    return a - b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))