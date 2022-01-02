from Chapter_3.Stack import Stack

if __name__ == "__main__":
    string = "SomeStringInReverse"
    reversed_string = ""
    s = Stack()
    print("String Before: %s" % string)
    #Add the string to the stack
    for character in string:
        s.push(character)

    #Print the string out
    while not s.isEmpty():
        reversed_string += s.pop()

    print("String After: %s" % reversed_string)