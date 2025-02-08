import csv
import numpy as np
from random import randrange
import matplotlib.pyplot as plt

def PopulateHouseData():
    with open("house_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        fields = ["size", "price"]

        writer.writerow(fields)
        for i in range(1, 20):
            size = randrange(i * 10, (i + 1) * 10) * randrange(1, 3)
            price = randrange(i * 10, (i + 10) * 10) * 10
            writer.writerow([size, price])

def GetHouseData():
    with open("house_data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        reader.__next__()
        return [[int(size), int(price)] for [size, price] in reader]

def PlotModel(*, args: dict, W: list[float], alpha: float):
    if (args.populate):
        PopulateHouseData()

    data = GetHouseData()
    n, cost = len(data), None
    X = np.array([x / 1000 for [x, _] in data])
    Y = np.array([y / 1000 for [_, y] in data])

    while cost == None or abs(cost) >= 0.042:
        Y_ = sum([W[i] * X ** i for i in range(len(W))])
        cost = sum([(Y_[i] - Y[i]) ** 2 for i in range(n)]) / (2 * n)
        print(cost, W)
        W_ = []
        for wi in range(len(W)):
            dw = sum([-(Y[i] - Y_[i]) * X[i] ** wi for i in range(n)]) / n
            W_.append(alpha * dw)
        W = [W[i] - W_[i] for i in range(len(W))]


    X_ = np.linspace(0, max(X))
    Y_ = sum([W[i] * X_ ** i for i in range(len(W))])

    plt.scatter(X, Y)
    plt.xlabel("Size")
    plt.ylabel("Price")
    plt.title("House Prices for Sizes")
    plt.grid(True)
    plt.plot(X_, Y_)
    plt.show()
