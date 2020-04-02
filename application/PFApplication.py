import sys

from numpy.distutils.fcompiler import none

from core.AppContext import AppContext


class PFApplication:

    def __init__(self):
        return

    def set_value(self, appcontext, arg, value):
        appcontext.set_dataset_name(value)

    def parse_args(self):
        #import core.AppContext
        appcontext = AppContext(train_dataset=none, test_dataset=none)
        argc = "-out=output -repeats=1 -trees=100 -r=1 -on_tree=true -export=1 -verbosity=0"
        argv = argc.split(" ")
        #print(argv)
        if len(argv) > 1:
            for i in range(1, len(argv)):
                options = argv[i].split("=")
                arg = options[0]
                value = options[1]
                self.set_value(appcontext, arg, value)
                print(appcontext.get_dataset_name())



pf = PFApplication()
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv[0]))
pf.parse_args()
print("Hola Mundo")