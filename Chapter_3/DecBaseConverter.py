from Chapter_3.Stack import Stack


def base_converter(number, base):
    digits = "0123456789ABCDEF"
    digits_stack = Stack()

    while number > 0:
        remainder = number % base
        digits_stack.push(remainder)
        number = number // base

    base_num_string = ""
    while not digits_stack.isEmpty():
        base_num_string += str(digits[digits_stack.pop()])

    return base_num_string


if __name__ == "__main__":
    user_input = input("FORMAT NUMBER:BASE\nEnter a number and base: ").split(":")
    in_number = int(user_input[0])
    in_base = int(user_input[1])
    base_num = base_converter(in_number, in_base)
    print("Number: %i Base: %i\nConverted Num: %s" % (in_number, in_base, base_num))
