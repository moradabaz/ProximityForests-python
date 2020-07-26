CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/PFApplication.py $CUR_DIR -name=$1 -train=$DATASET_DIR/"$1"_TRAIN.arff -test=$DATASET_DIR/"$1"_TEST.arff -targetlast=True -calculate=accuracy
echo "Classification process [ $1 ] finished"