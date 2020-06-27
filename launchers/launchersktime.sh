
#python3 ../PFAlternative.py $1
#path=$(pwd)
#python3 PFAlternative.py $path/datasets/Chinatown/Chinatown_TRAIN.arff $path/datasets/Chinatown/Chinatown_TEST.arff

CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/PFSktime.py $CUR_DIR -name=$1 -train=$DATASET_DIR/$1_TRAIN.arff -test=$DATASET_DIR/$1_TEST.arff -jobs=$2