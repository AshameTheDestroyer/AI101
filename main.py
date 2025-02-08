import argparse
from LinearRegression import PlotModel

parser = argparse.ArgumentParser()
parser.add_argument("--populate", type=bool, default=False)
args = parser.parse_args()

PlotModel(args=args, W=[0, 1, 1, 1], alpha=0.5)