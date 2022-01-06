class Node():
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, node):
        self.prev_node = node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node
