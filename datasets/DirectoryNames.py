import os
from sys import path

for i,j,y in os.walk('.'):
    print(i)


my_dirs = [d for d in os.listdir('.') if os.path.isdir(os.path.join('.', d))]

print(my_dirs)