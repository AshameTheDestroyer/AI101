import csv
import numpy as np
import matplotlib.pyplot as plt
from random import randrange, random

def PopulateHouseData():
    with open("house_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        fields = ["size", "price"]

        writer.writerow(fields)
        minimum, maximum = 1, 100
        for i in range(minimum, maximum + 1):
            size = randrange(i * 10, (i + 1) * 10)
            price = (size - (maximum - minimum) * 5) ** 3
            price *= randrange(1, 10)
            writer.writerow([size, price])

def GetHouseData():
    with open("house_data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        reader.__next__()
        return [[int(size), int(price)] for [size, price] in reader]

def PlotModel(*, populate: bool, degrees: int, alpha: float,  iteration: int | None = 10000):
    if (populate):
        PopulateHouseData()

    data = GetHouseData()
    n, cost = len(data), None
    X = np.array([x / 1000 for [x, _] in data])
    Y = np.array([y / 1000 for [_, y] in data])

    degrees += 1
    assert(degrees >= 1)
    W = [random() for _ in range(degrees)]

    for _ in range(iteration if iteration is not None else 0):
        Y_ = sum([W[i] * X ** i for i in range(degrees)])
        cost = sum([(Y_[i] - Y[i]) ** 2 for i in range(n)]) / (2 * n)
        print(cost)

        W_ = []
        for wi in range(degrees):
            dw = sum([-(Y[i] - Y_[i]) * X[i] ** wi for i in range(n)]) / n
            W_.append(alpha * dw)
        W = [W[i] - W_[i] for i in range(degrees)]


    X_ = np.linspace(0, max(X))
    Y_ = sum([W[i] * X_ ** i for i in range(degrees)])

    plt.scatter(X, Y)
    plt.xlabel("Size")
    plt.ylabel("Price")
    plt.title("House Prices for Sizes")
    plt.grid(True)
    if (iteration is not None):
        plt.plot(X_, Y_)
    plt.show()
