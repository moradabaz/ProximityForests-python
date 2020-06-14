import sys
sys.setrecursionlimit(31000)
from core import AppContext, ExperimentRunner
from distance.DistanceMeasure import DistanceMeasure
import timeit


class PFApplication:

    def __init__(self):
        self.appcontext = AppContext.AppContext(train_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv",
                                                test_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv")
        return

    def get_app_context(self):
        return self.appcontext

    def parse_args(self):
        argc = "-out=output -repeats=1 -trees=1 -r=1 -on_tree=true -export=1 -verbosity=2"
        argv = argc.split(" ")
        if len(argv) > 1:
            for i in range(1, len(argv)):
                options = argv[i].split("=")
                arg = options[0]
                value = options[1]
                self.appcontext.set_value(arg, value)


pf = PFApplication()
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv[0]))
pf.parse_args()
print("Hola Mundo")
pf.appcontext.print_content()
experimentrunner = ExperimentRunner.ExperimentRunner()
start = timeit.default_timer()
experimentrunner.run()
stop = timeit.default_timer()
print("Tiempo de ejecución TOTAL:", stop - start)
