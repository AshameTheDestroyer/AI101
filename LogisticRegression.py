import csv
import numpy as np
from random import randrange
import matplotlib.pyplot as plt

def PopulateHouseData():
    with open("student_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        fields = ["hours", "passed"]

        writer.writerow(fields)
        minimum, maximum = 4, 60
        for i in range(minimum, maximum + 1):
            hours = i
            passed = 1
            passed &= 0 if i < (maximum - minimum) / 3 or i > (maximum - minimum) * 4 / 5 or randrange(1, 10) > 7 else 1
            writer.writerow([hours, passed])

def GetStudentData():
    with open("student_data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        reader.__next__()
        return [[int(hours), int(passed)] for [hours, passed] in reader]

def PlotModel(*, args: dict, W: list[float], alpha: float, iteration: int = 10000):
    if (args.populate):
        PopulateHouseData()

    data = GetStudentData()
    n, cost = len(data), None
    X = np.array([x - np.median([x_ for [x_, _] in data]) for [x, _] in data])
    Y = np.array([y for [_, y] in data])

    for _ in range(iteration):
        Y_ = 1 / (1 + np.exp(-sum([W[i] * X ** i for i in range(len(W))])))
        cost = sum([-Y[i] * np.log(Y_[i]) - (1 - Y[i]) * np.log(1 - Y_[i]) for i in range(n)]) / n
        print(cost, W)
        W_ = []
        for wi in range(len(W)):
            dw = sum([-(Y[i] - Y_[i]) * X[i] ** wi for i in range(n)]) / n
            W_.append(alpha * dw)
        W = [W[i] - W_[i] for i in range(len(W))]

    X_ = np.linspace(min(X), max(X))
    Y_ = 1 / (1 + np.exp(-sum([W[i] * X_ ** i for i in range(len(W))])))

    plt.scatter(X, Y)
    plt.xlabel("Hours")
    plt.ylabel("Passed")
    plt.title("Student Passing According to Study Hours")
    plt.grid(True)
    plt.plot(X_, Y_)
    plt.show()
