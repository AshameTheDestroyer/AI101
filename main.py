import argparse
from LinearRegression import PlotModel as PlotLinearModel
from LogisticRegression import PlotModel as PlotLogisticModel

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="")
parser.add_argument("--populate", type=bool, default=False)
args = parser.parse_args()

match (args.model.lower()):
    case "linear":
        PlotLinearModel(populate=args.populate, degrees=3, alpha=1)
    case "logistic":
        PlotLogisticModel(populate=args.populate, degrees=2, alpha=0.001)