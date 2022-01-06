from Chapter_3.Lists_Review.UnorderedList.Node import Node


class UnorderedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def is_empty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.set_next_node(self.head)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.head = temp
        self.num_nodes += 1

    def length(self):
        """
        A length implementation that is O(1) requires a little extra heap memory to
        do this since we have to track the adding and removing of nodes
        :return: number of nodes in linked list
        """
        return self.num_nodes

    def search(self, data):
        """
        A search implementation that is O(n)
        :param data: item that we are searching for in the linked list
        :return: Boolean value of if the item was found or not
        """
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()
        return found

    def index(self, data):
        curr_index = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()
                curr_index += 1

        if found:
            return curr_index
        else:
            return False

    def remove(self, data):
        current = self.head
        previous = self.head
        found = False
        while previous is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()

        if found:
            previous.set_next_node(current.get_next_node())
            self.num_nodes -= 1

    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.set_next_node(temp)
            self.tail = temp
        self.num_nodes += 1

    def insert(self, pos, data):
        assert self.num_nodes > pos, "Index: %i is out of bounds" % (pos)
        curr_index = 0
        current = self.head
        previous = None
        temp = Node(data)

        if curr_index == 0:
            temp.set_next_node(self.head)
            self.head = temp
        elif (self.num_nodes - 1) == pos:
            self.tail.set_next_node(temp)
            self.tail = temp
        else:
            while current is not None and curr_index != pos:
                previous = current
                current = current.get_next_node()
                curr_index += 1

            previous.set_next_node(temp)
            temp.set_next_node(current)
        self.num_nodes += 1

    def pop(self, pos=None):
        if pos is None:
            assert not self.is_empty(), "No items in List"
            """
            Pop will be O(n) since this is not a doubly linked list
            :return: data
            """
            pos = 0
            current = self.head
            previous = None

            if self.num_nodes - 1 == pos:
                deleted_node = self.head
                self.head = None
                self.tail = None
            else:
                while pos != self.num_nodes - 1:
                    previous = current
                    current = current.get_next_node()
                    pos += 1

                deleted_node = previous.get_next_node()
                previous.set_next_node(None)
                self.tail = previous

        else:
            assert self.num_nodes - 1 >= pos, "Index: %i is out of bounds" % (pos)
            curr_index = 0
            current = self.head
            previous = None

            if pos == 0:
                deleted_node = self.head
                self.head = self.head.get_next_node()
            else:
                while current is not None and curr_index != pos:
                    previous = current
                    current = current.get_next_node()
                    curr_index += 1

                deleted_node = current
                previous.set_next_node(current.get_next_node())

        self.num_nodes -= 1

        return deleted_node.get_data()

    def __str__(self):
        if self.head is None:
            return "Head Node Id: %s\nNumber of Nodes: %i\n" % (None, self.length())
        else:
            return "Head Node Id: %s\nNumber of Nodes: %i\n" % (id(self.head), self.length())


if __name__ == "__main__":
    unordered_l = UnorderedList()

    print(unordered_l)

    for i in range(0, 50):
        unordered_l.append(i)

    print(unordered_l)

    while unordered_l.length() > 0:
        print("Size List Before Pop: %i" % (unordered_l.length()))
        popped_item = unordered_l.pop()
        print("Size List After Pop: %i\nItem Removed: %s\n" % (unordered_l.length(), popped_item))

    for i in range(0, 50):
        unordered_l.add(i)

    for i in range(0, 50):
        print("Does %i exists? %s" % (i, unordered_l.search(i)))

    for _ in range(50):
        print("Size List Before Pop: %i" % (unordered_l.length()))
        popped_item = unordered_l.pop(0)
        print("Size List After Pop: %i\nItem Removed: %s\n" % (unordered_l.length(), popped_item))

    print(unordered_l)
