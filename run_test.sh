#!/bin/bash

for name in checkpoint_14.pth.tar
do
YOUR_DATASET_FOLDER='data_volume/timecycle'

echo $name
if [ ! -d "results/davis_results__$name/" ]; then

    python test_davis.py \
    --evaluate --cropSize 320 --cropSize2 80 --gpu-id 0,1,2,3 --topk_vis 5 \
    --resume data_volume/timecycle/$name \
    --save_path results/davis_results__$name/
fi

python preprocess/convert_davis.py --in_folder results/davis_results__$name/ --out_folder results/davis_results__${name}_converted/ --dataset $YOUR_DATASET_FOLDER/davis/ && \
python $YOUR_DATASET_FOLDER/davis-2017/python/tools/eval.py -i results/davis_results__${name}_converted/ -o results/davis_results__${name}_converted/results.yaml --year 2017 --phase val \
| tee results/davis_results__${name}_converted/output.txt &

done
