CUR_DIR=$(cd .. && pwd)
for d in $CUR_DIR/datasets/*; do
  if [ -d $d ]; then
    dataset=$(basename $d)
    DATASET_DIR=$CUR_DIR/datasets/$dataset/
    echo ""
    python3 ../application/crossvalidation.py $CUR_DIR $dataset $DATASET_DIR/"$dataset"_TRAIN.arff
    echo "Classification process [ $dataset ] finished"
  fi
done

