from Chapter_3.Queue_Review.Queue import Queue

def hot_potato(list_names, nums):
    q = Queue()

    for name in list_names:
        q.enqueue(name)

    while q.size() > 1:
        for _ in range(nums):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

if __name__ == "__main__":
    names = ["John","Jake","James","Jerry","Alex","Brandon","Brandy","Mandy","Randy", "Jeff"]
    nums = 4
    winner = hot_potato(names, nums)
    print("The winner is: %s" % winner)
