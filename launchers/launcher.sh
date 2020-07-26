CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/AppRunner.py $CUR_DIR -name=$1 -train=$DATASET_DIR/"$1"_TRAIN.arff -test=$DATASET_DIR/"$1"_TEST.arff -repeat=1 -trees=35 -candidates=2 -targetlast=True -calculate=accuracy
echo "Classification process [ $1 ] finished"
