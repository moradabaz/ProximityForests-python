PForests (Gamma Version)

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
* Download the project
* Give full permissions to your project
* Go to the directory `launchers`
* Execute the following command:
   * `sh TermLauncherParam.sh [DATASET_NAME]`, where `[DATASET_NAME]` is the name of the dataset you have stored in the project. The Names available are:
        * `ItalyPowerDemand`
        * `MoteStrain`
        * `Plane`
        * `GesturePebbleZ2`
       
 * Try this example:
       - `sh TermLauncherParam.sh ItalyPowerDemand`



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
    
## Comparison with Sktime.ProximityForest

If you want to compare this Proximity Forest Project to the sktime project:
- Run the sh file `launchers/launchersktime.sh`, which can be found in the `launchers` directory, setting the following arguments:
   - `name`: The name of the dataset. The Names available are:
        * `ItalyPowerDemand`
        * `MoteStrain`
        * `Plane`
        * `GesturePebbleZ2`
        * `Chinatown`
        * `ERing`
        * `FacesUCR`
        * `FreezerRegularTrain`
        * `SmoothSubspace`
        * `ElectricDevices`
   - `trees`: The number of trees for the algorithm
   - `candidates`: Number of candidates per split
- Example:
   `sh launchersktime.sh Plane 20 3`
       
