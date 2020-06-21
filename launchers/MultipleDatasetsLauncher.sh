CUR_DIR=$(cd .. && pwd)
for d in $CUR_DIR/datasets/*; do
  if [ -d $d ]; then
    dataset=$(basename $d)
    DATASET_DIR=$CUR_DIR/datasets/$dataset/
    echo ""
    echo "Executing dataset [ $dataset ]  ..."
    python3 ../application/AppRunner.py $CUR_DIR -name=$dataset -train=$DATASET_DIR/"$dataset"_TRAIN.arff -test=$DATASET_DIR/"$dataset"_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
    echo "Classification process finished"
  fi
done

