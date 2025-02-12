import csv
import numpy as np
import matplotlib.pyplot as plt
from random import randrange, random

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

def PlotModel(*, populate: bool, degrees: int, alpha: float, iteration: int = 10000):
    if (populate):
        PopulateHouseData()

    data = GetStudentData()
    n, cost = len(data), None
    X = np.array([x - np.median([x_ for [x_, _] in data]) for [x, _] in data])
    Y = np.array([y for [_, y] in data])

    degrees += 1
    assert(degrees >= 1)
    W = [random() for _ in range(degrees)]

    for _ in range(iteration):
        Y_ = 1 / (1 + np.exp(-sum([W[i] * X ** i for i in range(degrees)])))
        cost = sum([-Y[i] * np.log(Y_[i]) - (1 - Y[i]) * np.log(1 - Y_[i]) for i in range(n)]) / n
        print(cost)
        W_ = []
        for wi in range(degrees):
            dw = sum([-(Y[i] - Y_[i]) * X[i] ** wi for i in range(n)]) / n
            W_.append(alpha * dw)
        W = [W[i] - W_[i] for i in range(degrees)]

    X_ = np.linspace(min(X), max(X))
    Y_ = 1 / (1 + np.exp(-sum([W[i] * X_ ** i for i in range(degrees)])))

    plt.scatter(X, Y)
    plt.xlabel("Hours")
    plt.ylabel("Passed")
    plt.title("Student Passing According to Study Hours")
    plt.grid(True)
    plt.plot(X_, Y_)
    plt.show()
