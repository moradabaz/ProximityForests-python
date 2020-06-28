CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
java -jar -Xmx1g ../application/ProximityForest.jar  -train=$DATASET_DIR/$1_TRAIN.csv -test=$DATASET_DIR/$1_TEST.csv -repeats=1 -trees=100 -r=5 -edistance=dtw