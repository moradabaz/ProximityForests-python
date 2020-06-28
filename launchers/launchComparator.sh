CUR_DIR=$(cd .. && pwd)
for d in $CUR_DIR/datasets/*; do
  if [ -d $d ]; then
    dataset=$(basename $d)
    DATASET_DIR=$CUR_DIR/datasets/$dataset/
    echo ""
    echo "Executing dataset [ $dataset ]  ..."
    python3 ../application/AppRunner.py $CUR_DIR -name=$dataset -train=$DATASET_DIR/"$dataset"_TRAIN.csv -test=$DATASET_DIR/"$dataset"_TEST.csv -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
    java -jar -Xmx1g ../application/ProximityForest.jar  -train=$DATASET_DIR/"$dataset"_TRAIN.csv -test=$DATASET_DIR/"$dataset"_TEST.csv -repeats=1 -trees=100 -r=5 -edistance=dtw
    echo "Classification process [ $dataset ] finished"
  fi
done

