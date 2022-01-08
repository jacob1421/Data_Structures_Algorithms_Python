from Chapter_3.Lists_Review.OrderedList.Node import Node
from random import randint


class OrderedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def add(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            curr_node = self.head

            while curr_node.get_data() <= data and curr_node.get_next_node() is not None:
                curr_node = curr_node.get_next_node()

            if curr_node is self.head:
                if self.head.get_data() <= data:
                    temp.set_prev_node(self.head)
                    if self.head.get_next_node() is not None:
                        temp.set_next_node(self.head.get_next_node())
                        self.head.get_next_node().set_prev_node(temp)
                    self.head.set_next_node(temp)
                else:
                    self.head.set_prev_node(temp)
                    temp.set_next_node(self.head)
                    self.head = temp
            elif curr_node is self.tail or curr_node.get_next_node() is None:
                if self.tail.get_data() <= data:
                    self.tail.set_next_node(temp)
                    temp.set_prev_node(self.tail)
                    temp.set_next_node(None)
                    self.tail = temp
                else:
                    self.tail.get_prev_node().set_next_node(temp)
                    temp.set_prev_node(self.tail.get_prev_node())

                    self.tail.set_prev_node(temp)
                    temp.set_next_node(self.tail)
            else:
                curr_node.get_prev_node().set_next_node(temp)
                temp.set_prev_node(curr_node.get_prev_node())

                curr_node.set_prev_node(temp)
                temp.set_next_node(curr_node)

        self.num_nodes += 1

    def remove(self, data):
        cur_node = self.head

        while cur_node is not None and cur_node.get_data() != data:
            cur_node = cur_node.get_next_node()

        if cur_node is None:
            return

        if cur_node is self.head:
            if self.head is self.tail:
                self.head = None
                self.tail = None
                self.num_nodes -= 2
                return
            else:
                cur_node.get_next_node().set_prev_node(None)
                self.head = cur_node.get_next_node()
        elif cur_node is self.tail:
            cur_node.get_prev_node().set_next_node(None)
            self.tail = cur_node.get_prev_node()
        else:
            cur_node.get_prev_node().set_next_node(cur_node.get_next_node())
            cur_node.get_next_node().set_prev_node(cur_node.get_prev_node())
        self.num_nodes -= 1

    def search(self, data):
        cur_node = self.head

        while cur_node is not None and cur_node.get_data() != data:
            cur_node = cur_node.get_next_node()

        return cur_node is not None

    def is_empty(self):
        return self.num_nodes == 0

    def length(self):
        return self.num_nodes

    def index(self, data):
        cur_node = self.head
        cur_idx = 0
        while cur_node is not None and cur_node.get_data() != data:
            cur_node = cur_node.get_next_node()
            cur_idx += 1

        if cur_node is not None:
            return cur_idx
        return False

    def pop(self, pos=None):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif pos is None:
            self.tail.get_prev_node().set_next_node(None)
            self.tail = self.tail.get_prev_node()
        else:
            assert self.num_nodes > pos, "Index: %i is out of bounds" % (pos)
            cur_node = self.head
            cur_idx = 0
            while pos != cur_idx and cur_node.get_next_node() is not None:
                cur_node = cur_node.get_next_node()
                cur_idx += 1

            if cur_node is self.head:
                cur_node.get_next_node().set_prev_node(None)
                self.head = cur_node.get_next_node()
            elif cur_node is self.tail:
                cur_node.get_prev_node().set_next_node(None)
                self.tail = cur_node.get_prev_node()
            else:
                cur_node.get_prev_node().set_next_node(cur_node.get_next_node())
                cur_node.get_next_node().set_prev_node(cur_node.get_prev_node())

        self.num_nodes -= 1

    def __str__(self):
        curr_node = self.head
        linked_list_str_visual = ""
        while curr_node is not None:
            linked_list_str_visual += (str(curr_node.get_data()) + " -> ")
            curr_node = curr_node.get_next_node()

        return linked_list_str_visual


if __name__ == "__main__":
    ordered_list = OrderedList()
    for _ in range(20):
        random_int = randint(0, 100)
        ordered_list.add(random_int)
        print(ordered_list)

    for _ in range(20):
        random_int = randint(0, 100)
        if ordered_list.search(random_int):
            print("The ordered list contain %i\n" % (random_int))

    for _ in range(20):
        random_int = randint(0, 100)
        if ordered_list.index(random_int) is not False:
            print("%i was found at index %i?\n" % (random_int, ordered_list.index(random_int)))

    print("\nLength Of List: %i\n" % (ordered_list.length()))
    for _ in range(20):
        ordered_list.pop()
        print(ordered_list)

    print("Length Of List: %i\n" % (ordered_list.length()))

    for x in range(20):
        ordered_list.add(x)

    while not ordered_list.is_empty():
        random_int = randint(0, 19)
        size_before_remove = ordered_list.length()
        ordered_list.remove(random_int)
        if ordered_list.length() != size_before_remove:
            print(ordered_list)

    print("Length Of List: %i\n" % (ordered_list.length()))

    for _ in range(20):
        random_int = randint(0, 100)
        ordered_list.add(random_int)
        print(ordered_list)

    print("Length Of List: %i\n" % (ordered_list.length()))

    print(ordered_list)
    ordered_list.pop(0)
    print(ordered_list)
    ordered_list.pop(ordered_list.length() - 1)
    print(ordered_list)
    ordered_list.pop(7)
    print(ordered_list)
    ordered_list.pop(5)
    print(ordered_list)

    print("Length Of List: %i\n" % (ordered_list.length()))

    # for _ in range(100):
    #     ordered_list = OrderedList()
    #
    #     for __ in range(500):
    #         random_int = randint(-1000, 1000)
    #         ordered_list.add(random_int)
    #
    #     check_node = ordered_list.head
    #     while check_node is not None and check_node.get_next_node() is not None:
    #         if check_node.get_data() > check_node.get_next_node().get_data():
    #             Exception("Error in Ordered List!")
    #
    #         check_node = check_node.get_next_node()
    #
    #     print(ordered_list)
