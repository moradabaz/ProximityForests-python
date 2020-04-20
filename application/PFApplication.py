import sys
from numpy.distutils.fcompiler import none
from core import AppContext, ExperimentRunner


class PFApplication:

    def __init__(self):
        self.appcontext = AppContext.AppContext(train_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv",
                                                test_dataset="/Users/morad/PycharmProjects/PForests/util/tabla1.csv")
        return

    def get_app_context(self):
        return self.appcontext

    def parse_args(self):
        argc = "-out=output -repeats=1 -trees=100 -r=5 -on_tree=true -export=1 -verbosity=2"
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
experimentrunner.run()
