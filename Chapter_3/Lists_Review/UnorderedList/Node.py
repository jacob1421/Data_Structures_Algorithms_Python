class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_next_node(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_next_node(self, node):
        self.next_node = node

    def set_data(self, data):
        self.data = data

    def __str__(self):
        if self.next_node is None:
            return "Node Id: %i\nNode Data: %s\nNext Node: %s\n" % (id(self), self.data, None)
        else:
            return "Node Id: %i\nNode Data: %s\nNext Node: %s\n" % (id(self), self.data, id(self.next_node))


if __name__ == "__main__":
    node_one = Node("Node 1 data")
    node_two = Node("Node 2 data")
    node_one.set_next_node(node_two)

    print(node_one)
    print(node_two)

    node_one.set_data("New node 1 data")
    node_two.set_data("New node 2 data")

    print(node_one)
    print(node_two)
