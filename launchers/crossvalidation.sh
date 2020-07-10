CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/crossvalidation.py $CUR_DIR $1 $DATASET_DIR/$1_TRAIN.arff
