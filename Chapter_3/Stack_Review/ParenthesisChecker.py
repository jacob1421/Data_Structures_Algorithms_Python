from Chapter_3.Stack_Review.Stack import Stack


def parChecker(check_string):
    balanced = True
    s = Stack()
    idx = 0
    while idx < len(check_string) and balanced:
        symbol = check_string[idx]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        idx += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    input_string = "(()())"
    isBalanced = parChecker(input_string)
    print("Does %s have balanced parenthesis? %s" % (input_string, isBalanced))
