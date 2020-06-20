CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/AppRunner.py $CUR_DIR -name=$1 -train=$DATASET_DIR/$1_TRAIN.csv -test=$DATASET_DIR/$1_TEST.csv -repeat=1 -trees=100 -candidates=5 -targetlast=True -ignoreFirst=False -calculate=accuracy
