from Chapter_3.Deque_Review.Deque import Deque

def palindrome_checker(word):
    dq = Deque()
    is_palindrome = True
    for c in word:
        dq.add_front(c)

    while dq.size() > 1 and is_palindrome:
        if dq.remove_rear() != dq.remove_front():
            is_palindrome = False

    return is_palindrome


if __name__ == "__main__":
    user_input = input("Please enter a word: ")
    is_palindrome = palindrome_checker(user_input)
    print("%s is a palindrome? %s" % (user_input, is_palindrome))