PForests (Gamma Phase)

This is the Proximity Forest algorithm implemented to classify Time Series.

Requirements:
- You can only run this project if you have a UNIX-based OS (Linux or OSX)
- You must have python3.7
- Give full permission to your project directory and files
- We recommend you locate your project in your `$HOME` directory.

Packages to Install Previously:
   - `pip install dtaidistance` or `pip3 install dtaidistance`
   - `pip install -v --force-reinstall --no-deps --no-binary dtaidistance dtaidistance`
   - `pip install scipy` or `pip3 install scipy`


How to run a simple execution:
* Open the file `AppRunner.py` in your `application` directory.
* Set the full path of your project in the second line of the file `AppRunner.py`
    *  `sys.path.append("[Absolute path of your project directory]")`
* Open the `sh` script `TermLauncher.sh` in the folder `/application`:
    * Change the variable `$DATASET_DIR` and write the full path of the datasets directory.
    `$DATASET_DIR=[YOUR_PROJECT_FULL_PATH]/dataset`.
    * To run the `TermLauncher.sh` script you have to pass a parameter which is the name of the dataset. The Following names you have available are:
        * `ItalyPowerDemand`
        * `MoteStrain`
        * `Plane`
        * `GesturePebbleZ2`
       
    * Run this example:
        - `sh TermLauncher.sh ItalyPowerDemand`



Parameters of python execution:
- Run the sh file `application/TermLauncher.sh` setting the following parameters:
 - `name`: The name of the experiment
 - `-train`: The training dataset path. It must have a `.ts` or `.arff` extension.
 - `-test`: The testing dataset path. It must have a `.ts` or `.arff` extension.
 - The training and testing datasets can be found in the folder `datasets/`
 - `-repeat`: Number of repeats of the experiment
 - `-trees`: Number of trees of the PForest
 - `-candidates`: Number of candidates per tree
 - `-targetlast`: It indicates if the last column of the dataset is the class of the serie. 
    - P.e. if the line is `0.32, 0.45, ..., -0.12, X_AXIS`, setting `-targetlast=True` means the `X_AXIS` is the series class and it's located in the last column
    
