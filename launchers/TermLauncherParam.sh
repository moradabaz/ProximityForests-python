#python AppRunner.py -name=MoteStrain -train=/Users/morad/Desktop/resultados/MoteStrain/MoteStrain_TRAIN.arff -test=/Users/morad/Desktop/resultados/MoteStrain/MoteStrain_TRAIN.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPower -train=/Users/morad/Desktop/resultados/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff -test=/Users/morad/Desktop/resultados/ItalyPowerDemand/ItalyPowerDemand_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPowerDemand -train=/Users/morad/PycharmProjects/PForests/datasets/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff -test=/Users/morad/PycharmProjects/PForests/datasets/ItalyPowerDemand/ItalyPowerDemand_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
#python AppRunner.py -name=ItalyPowerDemand -train=/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TRAIN.csv -test=/Users/morad/Downloads/ItalyPowerDemand/ItalyPowerDemand_TEST.csv -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=all
CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/AppRunner.py $CUR_DIR -name=$1 -train=$DATASET_DIR/$1_TRAIN.arff -test=$DATASET_DIR/$1_TEST.arff -repeat=1 -trees=100 -candidates=5 -targetlast=True -calculate=accuracy
