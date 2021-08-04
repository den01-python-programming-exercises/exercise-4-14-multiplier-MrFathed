from multiplier import Multiplier

def main():
    #write your code below this line
    multiply_by_three = Multiplier(3)

    print("multiply_by_three.multiply(2): " + str(multiply_by_three.multiply(2)))

    multiply_by_four = Multiplier(4)

    print("multiply_by_four.multiply(2): " + str(multiply_by_four.multiply(2)))
    print("multiply_by_three.multiply(1): " + str(multiply_by_three.multiply(1)))
    print("multiply_by_four.multiply(1): " + str(multiply_by_four.multiply(1)))


if __name__ == '__main__':
    main()
