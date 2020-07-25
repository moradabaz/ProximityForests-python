#python AppRunner.py -name=MoteStrain -train=/Users/morad/Desktop/resultados/MoteStrain/MoteStrain_TRAIN.arff -test=/Users/morad/Desktop/resultados/MoteStrain/MoteStrain_TRAIN.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPower -train=/Users/morad/Desktop/resultados/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff -test=/Users/morad/Desktop/resultados/ItalyPowerDemand/ItalyPowerDemand_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPowerDemand -train=/Users/morad/PycharmProjects/PForests/datasets/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff -test=/Users/morad/PycharmProjects/PForests/datasets/ItalyPowerDemand/ItalyPowerDemand_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPowerDemand -train=/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TRAIN.csv -test=/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TEST.csv -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=all
CUR_DIR=$(cd .. && pwd)
for d in $CUR_DIR/datasets/*; do
  if [ -d $d ]; then
    dataset=$(basename $d)
    DATASET_DIR=$CUR_DIR/datasets/$dataset/
    CUR_DIR=$(cd .. && pwd)
    DATASET_DIR=$CUR_DIR/datasets/$dataset/
    python3 ../application/PFApplication.py $CUR_DIR -name=$dataset -train=$DATASET_DIR/"$dataset"_TRAIN.arff -test=$DATASET_DIR/"$dataset"_TEST.arff -targetlast=True -calculate=accuracy
    echo "Classification process [ $dataset ] finished"
  fi
done