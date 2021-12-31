"""
EXPERIMENT:
This experiment explores a number of methods that you can use to generate a list of numbers. More importantly, we are exploring the time
complexity of each method used to generate the list of numbers.


RESULTS:
concat  1.0740851999999999 milliseconds
append  0.10977720000000013 milliseconds
comprehension  0.0516972 milliseconds
list range  0.007764699999999847 milliseconds

CONCLUSION:
According to the experiment results, the 'range' function would be the best choice in generating a list of numbers.
"""

from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

if __name__ == "__main__":
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print("append ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print("list range ", t4.timeit(number=1000), "milliseconds")