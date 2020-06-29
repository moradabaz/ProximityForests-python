CUR_DIR=$(cd .. && pwd)
#for dataset in Chinatown ERing ItalyPowerDemand SmoothSubspace; do
DATASET_DIR=$CUR_DIR/datasets/$1
for trees in 10 20 50 100
do
  for candidates in 2 3 4 5; do
    echo ""
    echo "Executing dataset [ $1 ]  ..."
    python3 ../application/AppRunner.py $CUR_DIR -name=$1 -train=$DATASET_DIR/$1_TRAIN.csv -test=$DATASET_DIR/$1_TEST.csv -repeat=1 -trees=$trees -candidates=$candidates -targetlast=True -calculate=accuracy
    echo "Classification process [ $1 ] finished"
  done
done

