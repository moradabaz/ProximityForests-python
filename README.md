PForests (Gamma Phase)

This is the Proximity Forest algorithm implemented to classify Time Series.


How to run the project:
- You can only run this project if you have a UNIX-based OS (Linux or OSX)
- Download the project
- In the python file `application/AppRunner.py`, in the second line, you have
to establish the system path, in other words, the full path of your main project folder.
    - P.e. if your project folder is "~/Desktop/PForest", you have to write `sys.path.append("/Users/home/Desktop/PForests/")`
- Download the following packages:
    - `pip install dtaidistance` or `pip3 install dtaidistance`
    - `pip install numpy` or `pip install numpy`
- Run the sh file `application/TermLauncher.sh` setting the following parameters:
 - `name`: The name of the experiment
 - `-train`: The training dataset path. It must have a `.ts` or `.arff`.
 - `-test`: The testing dataset path. It must have a `.ts` or `.arff`.
 - The training and testing datasets can be found in the folder `datasets/`
 - `-repeat`: Number of repeats of the experiment
 - `-trees`: Number of trees of the PForest
 - `-candidates`: Number of candidates per tree
 - `-targetlast`: It indicates if the last column of the dataset is the class of the serie. 
    - P.e. if the line is `0.32, 0.45, ..., -0.12, X_AXIS`, setting `-targetlast=True` means the `X_AXIS` is the series class and it's located in the last column
    
Simple execution:

* Set the full path of your project in the second line of the file `application/AppRunner.py`
    *  ex. `sys.path.append("Absolute path of your project folder")`
* Copy the full paths of the training and testing datasets in the folder `datasets`
* Run the `/TermLauncher.sh` file in the folder `/application`