class Maths:

    def __init__(self): pass

    @staticmethod
    def infinite_sum(start, end, function):
        result = 0.0

        for i in range(start, end+1, 1):
            result += function(i)

        return result

    @staticmethod
    def factorial(n):
        f = 1
        while n > 0:
            f = f * n
            n = n-1
        return f

    @staticmethod
    def Combination(n, r):
        result = Maths.factorial(n)/(Maths.factorial(r)*Maths.factorial(n-r))

        return result

    @staticmethod
    def convertToDecimal(fraction):
        fraction = str(fraction)
        numbers = [1, 1]
        for item in fraction:
            if item == '/':
                numbers = fraction.split('/')
                print (numbers)
                continue
        if len(numbers)<2:
            return float(fraction)
        else:
            return float(numbers[0]) / float(numbers[1])
