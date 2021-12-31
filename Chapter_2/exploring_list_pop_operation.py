from timeit import Timer
import matplotlib.pyplot as plt

if __name__ == "__main__":
    popzero = Timer("x.pop(0)", "from __main__ import x")
    popzero_data = []

    popend = Timer("x.pop()", "from __main__ import x")
    popend_data = []

    print("%15s %15s %15s" % ("pop(0)", "pop()", "i"))
    for i in range(1000000, 21000000, 1000000):
        x = list(range(i))
        pt = popend.timeit(number=1000)
        popend_data.append((i, pt))

        x = list(range(i))
        pz = popzero.timeit(number=1000)
        popzero_data.append((i, pz))
        print("%15.5f, %15.5f %15i" % (pz, pt, i))

    x, y = zip(*popzero_data)
    plt.plot(x, y, '-o', color='blue', label='Pop(0)')

    x, y = zip(*popend_data)
    plt.plot(x, y, '-o', color='green', label='Pop()')
    plt.xlabel("Time (Milliseconds)")
    plt.ylabel("No. of Records (Million)")
    plt.legend()
    plt.title('List - Pop(0) vs Pop()')
    plt.savefig("popend_vs_popzero.png")