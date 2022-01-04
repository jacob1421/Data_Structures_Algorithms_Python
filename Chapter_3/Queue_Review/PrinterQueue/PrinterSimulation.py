from Chapter_3.Queue_Review.Queue import Queue
from Chapter_3.Queue_Review.PrinterQueue.Printer import Printer
from Chapter_3.Queue_Review.PrinterQueue.Task import Task
from random import randrange


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_q = Queue()
    wait_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_q.enqueue(task)

        if (not lab_printer.busy()) and (not print_q.is_empty()):
            next_task = print_q.dequeue()
            wait_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    avg_wait = sum(wait_times) / len(wait_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (avg_wait, print_q.size()))


def new_print_task():
    num = randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)
