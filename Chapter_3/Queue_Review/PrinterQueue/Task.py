from random import randrange


class Task:
    def __init__(self, time):
        self.timetamp = time
        self.pages = randrange(1, 21)

    def get_stamp(self):
        return self.timetamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timetamp
