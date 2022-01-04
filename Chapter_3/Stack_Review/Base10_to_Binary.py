from Chapter_3.Stack_Review.Stack import Stack


def convert_base_10_to_binary(base_10_number):
    bin_stack = Stack()

    while base_10_number > 0:
        remainder = base_10_number % 2
        bin_stack.push(remainder)
        base_10_number = base_10_number // 2

    bin_num = ""
    while not bin_stack.is_empty():
        bin_num += str(bin_stack.pop())

    return bin_num


if __name__ == "__main__":
    user_input = int(input("Enter a number you want to convert to binary: "))
    bin_num = convert_base_10_to_binary(user_input)
    print("Number entered: %i\nBinary number: %s" % (user_input, bin_num))
